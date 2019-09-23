from xml.etree import ElementTree as et
import os
import traceback as trace

for filename in os.listdir(path="C:\\Users\\Arge\\Desktop\\XmlToPdf\\xml"):
    if filename.endswith(".xml"):
        root = et.parse("xml/" + filename).getroot()
        for element in root[0][1][0]:
            if element.find("Denominazione") != None:
                denominazione = element.find("Denominazione").text
                break

        for element in root[1][0]:
            if element.find("Data") != None:
                data = element.find("Data").text
                numero = element.find("Numero").text
                break
    
        try:
            with open("C:\\Users\\Arge\\Desktop\\XmlToPdf\\txt\\" + data + "_" + denominazione + "_" + numero + ".txt", "w") as f:
                f.write("----------------------------- TESTA FATTURA -----------------------------\n")
                for element in root.iter("*"):
                    if element.tag == "DatiTrasmissione" or element.tag == "CedentePrestatore" or element.tag == "CessionarioCommittente":
                        f.write("\n:> " + element.tag + "\n")
                    elif element.tag == "FatturaElettronicaBody":
                        f.write("\n\n----------------------------- DETTAGLIO FATTURA -----------------------------\n\n")
                    elif element.tag == "NumeroLinea":
                        f.write("\n")
                    elif element.tag == "Allegati":
                        break

                    if len(element.getchildren()) == 0:
                        f.write(element.tag + ": " + element.text + "\n")
        except:
            trace.print_exc()
            continue
                