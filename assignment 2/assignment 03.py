def mohit_mostatil(tol,arz):
    mohit= (tol+arz)*2
    return (mohit) 

def masahat_mostatil(tol,arz) :
    masahat= (tol*arz)
    return (masahat)

if __name__  == '__main__':
    while True :
        try:
            tol= int(input("tol ra be shecle cm vared konid:"))
            arz= int(input('arz ra be shecle cm vared konid:'))

            masahat = masahat_mostatil(arz, tol)
            mohit = mohit_mostatil(arz, tol)
        
            print(f"masahat_mostatil:{masahat}")
            print(f"mohit_mostatil:{mohit}") 

            break

        except ValueError :
            print ("lotfan adad vared konid")
            continue

        except Exception as e:
            print(f"\nAn error has occured:\n{e}")
            continue


