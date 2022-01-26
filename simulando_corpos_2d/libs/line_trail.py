class Trail:
    def __init__(self, color=(255,255,255), thickness=1) -> None:
        self.color = color
        self.thickness = thickness
        self.trass = []
        self.last_place = None

        #Configs-------------
        self.separacao = 15
        self.n_trass = 20
        #--------------------

        self.control_separacao = self.separacao
    
    def update(self, place):
        if not self.control_separacao:
            if len(self.trass) > self.n_trass: 
                self.trass.remove(self.trass[0])
            if self.last_place:
                self.new_trass(self.last_place[:], place[:])
            else:
                self.last_place = place[:]
            self.control_separacao = self.separacao
        else:
            self.control_separacao -= 1
        
        self.last_place = place[:]
    
    def new_trass(self, pt1, pt2):
        self.trass.append(
            {
                'pt1':pt1,
                'pt2':pt2,
                'color':self.color,
                'thickness':self.thickness,
            }
        )
    