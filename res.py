import PyPDF2
fil=open("resultcse.pdf","rb");
reso=PyPDF2.PdfFileReader(fil)
n=reso.numPages
#print(str)
c=0
ans=0
for j in range(0,n):
    p=reso.getPage(j)
    str=p.extractText()
    for i in range(3,(len(str)-4)):
            k=""
            k=str[i:i+4]
            if(k[1]=='.' and str[i-1].isdigit()==1 and str[i+3].isdigit()==1 and str[i+2].isdigit()==1 and str[i-2].isdigit()==1 and str[i-3]=='.'):
                    #print(k)
                    #print("\n")
                    c=c+1
                    ans=ans+float(k)
print("Tot Number of Students in class=",c)
print("Avg gpa of class=",ans/c)







#pos1=str.find("22.00")
#pos2=str.find("1.61")
#print(str[pos1:pos2])
#we want 131 132 133 and 134





