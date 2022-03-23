def hitungKonsonan(self):         
        k = self.teks
        vokal = 'aiueoAIUEO'
        jum = 0
        for i in k :
            if i.lower() not in vokal:
                jum += 1
        return jum
