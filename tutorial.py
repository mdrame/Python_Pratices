# understanding class and object 


#my dad class
class Dad():
    # constructor method
    def __init__(self, last_name, race, height, date_of_birth):
        self.last_name = last_name
        self.race = race
        self.height = height
        self.date_of_birth = date_of_birth

# Me class inheriting from Dad class.
class Me(Dad):
    # constructor method
    def __init__(self, last_name, race, height, date_of_birth, sex ):
        # super.__init__ so we don't got to call self. on ever parameter
        super().__init__(last_name, race, height, date_of_birth)
        self.sex = sex

    def walking(self):
        return "Walking"

my_dad = Dad("Amara", "Black", "5-10", 1924)

me = Me(my_dad.last_name, my_dad.race,  6, 1950, "Male")


print(f"\n{my_dad}\n")
print("Dad:\n\n\n\n\n\n\n")

print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")

print("Me:")
print(f"\n{me.walking()}\n\n\n\n\n\n\n\n\n")

















