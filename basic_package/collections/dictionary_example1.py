import datetime

def display_dictionary(dictionary):
    for key,value in dictionary.items():
        print(f"la valeur du key={key} et la valeur du value= {value}")


def Main():
    dictionary={"nom":"carlos","date":datetime.datetime(2000, 5, 25),"poids_kg":20}
    display_dictionary(dictionary)

if __name__ == "__main__":
    Main()