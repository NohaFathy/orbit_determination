''' 
NSST - intro to orbital mechanics3 
Gibb's methos of preliminary orbit determination

'''

import numpy as np
from numpy.linalg import norm
import math 


def gibbs(R1, R2, R3, mu=398600):
    # step1 Normalize pos vectors
    r1 = norm(R1)
    r2 = norm(R2)
    r3 = norm(R3)

    # step2 Calc C vecs
    C12 = np.cross(R1, R2)
    C23 = np.cross(R2, R3)
    C31 = np.cross(R3, R1)

    # step3 verify pos vecs are co-planar
    uR1 = R1 / r1
    uC23 = C23 / norm(C23)

    COPLANAR = True if np.dot(uR1, uC23) < abs(0.005) else False
    

    if COPLANAR:
        # step4  find N, D, S
        N = r1 * C12 + r2 * C23 + r3 * C31
        n = norm(N)

        D = C12 + C23 + C31
        d = norm(D)

        S = R1 * (r2 - r3) + R2 * (r3 - r1) + R3 * (r1 - r2)

        R = [R1, R2, R3]
        r = [r1, r2, r3]

        V = []
        for i, pos in enumerate(R):
            V.append(np.sqrt(mu / (n * d)) * (np.cross(D, pos) / r[i] + S))

        return V

    else:
        raise Exception("positions vecs given are not co-planar")
    





def main( mu=398600):
    k_vector = ([0,0,1])
    R1 = np.array([5887, -3520, -1204])
    R2 = np.array([5572, -3457, -2376])
    R3 = np.array([5088, -5000, -3480])
    V = gibbs(R1, R2, R3)
    v = []

    for vec in V:
        v.append(norm(vec))
    
    print(f"The speed at R2 is {v[1]:.2f} km/s")

    #Calc semi-major axis 

    eta=v[1]**2/2 - mu/norm(R1)    #orbit energy equation
    a = -mu/2*eta
    print (f"semi-major axis of the orbit is { a :.2f} km" )

    # Calc eccentricity vector 
    h  = np.cross(R1,V[1])      # angular momentum vector 

    e_vector = (np.cross(V[1],h )/mu ) - (R1/norm(R1))
    e = norm(e_vector )
    print(f" the eccentricity of the orbit is { e :.2f} ")


    #Calc inclination angle
    i = math.acos((np.dot(h,k_vector)) / (norm(h)))
    print (f"the inclination of the orbit is {  i:.2f} degree")


    #Calc true anomaly 
    seta = math.acos((np.dot(e_vector,R1)) / (np.dot(e,norm(R1))))
    print (f" true anomaly = {seta:.2f} degree")

    return
    




if __name__ == "__main__":
    main()




            



    









