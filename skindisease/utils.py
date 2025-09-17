import os
import re
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .ontologija import NS 



def razdvoji_rijeci(value):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', value)


def pronadji_dijagnoze(graf, simptomi, dijelovi_tijela):
    dijagnoze_info = []

    for simptom in simptomi:
        for dio in dijelovi_tijela:
            query = f"""
            SELECT ?oboljenje WHERE {{
                ?oboljenje <{NS}ima_simptom> <{NS}{simptom}> .
                ?oboljenje <{NS}pojavljuje_se_na> <{NS}{dio}> .
            }}
            """
            for row in graf.query(query):
                dijagnoza = str(row[0]).split("/")[-1]
                
                if not any(d['dijagnoza'] == dijagnoza for d in dijagnoze_info):
                    tretmani = {
                        str(tretman[0]).split("/")[-1]
                        for tretman in graf.query(f"""
                            SELECT ?tretman WHERE {{
                                <{NS}{dijagnoza}> <{NS}preporučuje_tretman> ?tretman .
                            }}""")
                    }
                    
                    okidaci = {
                        str(okidac[0]).split("/")[-1]
                        for okidac in graf.query(f"""
                            SELECT ?okidac WHERE {{
                                ?okidac <{NS}pogoršava> <{NS}{dijagnoza}> .
                            }}""")
                    }
                    
                    dijagnoze_info.append({
                        'dijagnoza': dijagnoza,
                        'tretmani': list(tretmani),
                        'okidaci': list(okidaci)
                    })
    
    return dijagnoze_info

def generiraj_pdf(username, dijagnoze_info):
    user_media_uploads_folder = os.path.join(settings.MEDIA_ROOT, 'uploads', username)
    os.makedirs(user_media_uploads_folder, exist_ok=True)
    
    pdf_path_on_disk = os.path.join(user_media_uploads_folder, 'dijagnoza.pdf')
    
    width, height = letter 
    margin = 1 * inch

    c = canvas.Canvas(pdf_path_on_disk, pagesize=letter)

    c.setFont("Helvetica-Bold", 18) 
    c.drawCentredString(width / 2.0, height - margin, "SkinSync - Rezultati Dijagnoze")

    
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2.0, height - margin - 20, f"Za korisnika: {username}")
    
    c.line(margin, height - margin - 35, width - margin, height - margin - 35)

    y_position = height - margin - 60

    if not dijagnoze_info:
        c.setFont("Helvetica-Oblique", 12) 
        c.drawString(margin, y_position, "Nije pronađena nijedna dijagnoza za odabrane simptome.")
        c.save()
        return pdf_path_on_disk

    for item in dijagnoze_info:
        if y_position < margin + 100: 
            c.showPage() 
            y_position = height - margin 


        c.setFont("Helvetica-Bold", 14)
        dijagnoza_tekst = razdvoji_rijeci(item['dijagnoza'])
        c.drawString(margin, y_position, dijagnoza_tekst)
        y_position -= 25 

        
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margin, y_position, "Preporučeni tretmani:")
        y_position -= 15
        c.setFont("Helvetica", 10)
        tretmani_lista = [razdvoji_rijeci(t) for t in item.get('tretmani', [])]
        for tretman in tretmani_lista:
            c.drawString(margin + 15, y_position, f"- {tretman}")
            y_position -= 14

       
        okidaci_lista = [razdvoji_rijeci(o) for o in item.get('okidaci', [])]
        if okidaci_lista:
            y_position -= 10 
            c.setFont("Helvetica-Bold", 11)
            c.drawString(margin, y_position, "Izbjegavajte sljedeće okidače:")
            y_position -= 15
            c.setFont("Helvetica", 10)
            for okidac in okidaci_lista:
                c.drawString(margin + 15, y_position, f"- {okidac}")
                y_position -= 14
        
        y_position -= 30


    c.save()
    return pdf_path_on_disk
