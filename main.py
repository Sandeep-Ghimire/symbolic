import abc
class AbstractPolynomial(metaclass=abc.ABCMeta):

    def __init__(self,list_of_pairs=[]):
        "takes list of (coeff,power) pairs and construct polynomial"

        #sort by power (power is at index 1 of pair)
        self._poly = sorted(list_of_pairs,key=lambda pair: pair[1])
        self.simplify()

    def max_degree(self):
        if self._poly == []:
            return 0
        return max(self._poly,key=lambda pair:pair[1])[1]

    def min_degree(self):
        if self._poly == []:
            return 0
        return min(self._poly,key=lambda pair: pair[1])[1]


    def _get_terms_with(self,power):
        return list(filter(lambda pair: pair[1] == power,self._poly))  

        
    def __repr__(self):
        "This is the default representation"
        def stringify_term(pair):

            def adapted_abs(coeff):
                "abs that handles empty string"
                return "" if coeff == 1 else abs(coeff)

            coeff,power = pair
            sign = '+' if coeff > 0 else '-'
            coeff = adapted_abs(coeff)
            if power > 1 or power < 0:
                return f"{sign}{coeff}x^{power}"
            elif power == 0:
                return f"{sign}{coeff}"
            elif power == 1:
                return f"{sign}{coeff}x"

        repr_str = "".join(map(stringify_term,self._poly))
        return repr_str if len(repr_str) > 0 and repr_str[0]=='-' else repr_str[1:]

    def simplify(self):
        "default simplification routine"
        def has_nonzero_coeff(pair):
            coeff,_=pair
            return coeff != 0
        

        #add coeffs of same powered terms
        result_terms = []
        for power in range(self.min_degree(),self.max_degree()+1):
            same_power_terms = self._get_terms_with(power)
            result_term = (0,power)
            for coeff,_ in same_power_terms:
                result_term = result_term[0]+coeff,result_term[1]
            result_terms.append(result_term)
    #filter elements with non zero coeffs
        self._poly = list( filter(has_nonzero_coeff,result_terms))
        
            

    @abc.abstractmethod
    def __add__(self,other):
        pass

    @abc.abstractmethod
    def __sub__(self,other):
        pass

    @abc.abstractmethod
    def __eq__(self,other):
        pass

    @abc.abstractmethod
    def __mul__(self,other):
        pass


class Polynomial(AbstractPolynomial):

    def __add__(self,other):
        return Polynomial(self._poly+other._poly)

    def __sub__(self,other):
        return Polynomial(self._poly + other.neg()._poly)

    def __mul__(self,other):
        product_list = [Polynomial._multterm(t1,t2)
                        for t1,t2 in Polynomial.generate_pairs(self,other)]
        return  Polynomial(product_list)
        

    def __eq__(self,other):
        return self._poly == other._poly

    def _mapterm(self,func):
        self._poly = list( map(func,self._poly))

    def _clone(self):
        return Polynomial(self._poly)

    def neg(self):
        p = self._clone()
        p._mapterm(lambda pair:(-pair[0],pair[1])) #make negative coefficients
        return p

    @staticmethod
    def _multterm(pair1,pair2):
        coeff1,exp1 = pair1
        coeff2,exp2 = pair2
        return (coeff1*coeff2,exp1+exp2)

    @staticmethod
    def generate_pairs(p1,p2):
        for term1 in p1._poly:
            for term2 in p2._poly:
                yield (term1,term2)




def split_by(string,func):
    prev_pos = 0
    cur_pos = 0
    splitted = []
    while (cur_pos < len(string)):
        char = string[cur_pos]
        if func(char):
            splitted.append(string[prev_pos:cur_pos])
            prev_pos = cur_pos
        cur_pos += 1
    splitted.append(string[prev_pos:cur_pos])
    return splitted


        

