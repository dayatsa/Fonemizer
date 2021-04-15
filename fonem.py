from arpabetandipaconvertor.phoneticarphabet2arpabet import PhoneticAlphabet2ARPAbetConvertor
import pandas as pd
import numpy as np

class IndoARPA():
    def __init__(self, path='dataset/ipa-data.csv', separator=' ', res_ipa=False):
        self.data_ipa = self.getDataIPA(path)
        self.separator = separator
        self.convert = PhoneticAlphabet2ARPAbetConvertor()
        self.res_ipa = res_ipa


    def getDataIPA(self, path):
        df = pd.read_csv(path)
        self.x = df.iloc[:,1]
        self.y = df.iloc[:,2]
        self.x = self.x.to_numpy()
        self.y = self.y.to_numpy()


    def indo2IPA(self, str_in):
        result_ipa = ""
        temp = ""
        chr_before = ""
        two_chr = False
        
        for chr in str_in:
            is_symbol = False
            temp = ""
            
            # fix ng in indonesia
            if chr_before == 'n' and chr == 'g':
                chr = 'ng'
                two_chr = True
            
            # fix ao in indonesia
            elif chr_before == 'a' and chr == 'o':
                chr = 'ɔ'
                two_chr = True
            
            # fix au in indonesia
            elif chr_before == 'a' and chr == 'u':
                chr = 'au'
                two_chr = True      
            
            # fix ai in indonesia
            elif chr_before == 'a' and chr == 'i':
                chr = 'ai'
                two_chr = True 
            
            # fix dh in indonesia
            elif chr_before == 'd' and chr == 'h':
                chr = 'ð'
                two_chr = True   
            
            # fix sy in indonesia
            elif chr_before == 's' and chr == 'y':
                result_ipa = result_ipa[:-1]     
                result_ipa += 'ʃ'
            
            elif chr_before == '' and chr == 'a':
                chr = 'ʌ'
            
            if chr == ' ':
                temp = ' '
        
            elif chr == '.':
                temp = '.'
                is_symbol = True
        
            elif chr == ',':
                temp = ','
                is_symbol = True
            
            else: 
                for i in range(self.x.shape[0]):
                    if chr == self.x[i]:
                        temp = self.y[i]

            if two_chr:
                result_ipa = result_ipa[:-1]
                two_chr = False

            if is_symbol == True:
                pass
            else:  
                result_ipa += temp
                chr_before = chr

        return result_ipa 

    
    def indo2ARPA(self, str_in):     
        result_arpa = ""
        result_ipa = self.indo2IPA(str_in)
        # print(result_ipa)
        two_char = False
        two_char_str = ""

        for chr in result_ipa:
            # print(chr)
            if chr == 'a':
                two_char = True
                two_char_str = chr
        
            else:
                if two_char == True:
                    chr = two_char_str + chr
                    two_char = False
                    two_char_str = ""
                
                if chr == ' ':
                    result_arpa += ' '
                else:
                    result_arpa += self.convert.convert(chr) + self.separator 
        if self.res_ipa == True:    
            return result_ipa, result_arpa 
        else:
            return result_arpa 
