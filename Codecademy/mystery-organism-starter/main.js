/* 
codecademy extract:

Context: You’re part of a research team that has found a new mysterious organism at the bottom of the ocean near hydrothermal vents. 
Your team names the organism, Pila aequor (P. aequor), and finds that it is only comprised of 15 DNA bases. The small DNA samples and 
frequency at which it mutates due to the hydrothermal vents make P. aequor an interesting specimen to study. However, P. aequor cannot 
survive above sea level and locating P. aequor in the deep sea is difficult and expensive. Your job is to create objects that simulate 
the DNA of P. aequor for your research team to study.

*/
// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G']
  return dnaBases[Math.floor(Math.random() * 4)] 
}

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = []
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase())
  }
  return newStrand
}

//pAequor specimen factory
const pAequorFactory = (num,dna) => {
  return {
    specimenNum:num,
    dna:dna,
    mutate() {
      let dnaBases = ['A', 'T', 'C', 'G']
      const randBaseIndex = Math.floor(Math.random() * 14)
      const baseToMutate = this.dna[randBaseIndex]
      //remove the dna base at the given random index from the 
      //dnaBases array so a new random one can be assigned
      dnaBases.splice(dnaBases.indexOf(baseToMutate),1) 
      const newRandBase = dnaBases[Math.floor(Math.random() * 3)]
      this.dna[randBaseIndex] = newRandBase
    },
    compareDNA(pAequor) {
      //compares the DNA of this specimen with another
      let matches = 0
      for (i=0;i<pAequor.dna.length;i++) {

        if (this.dna[i] === pAequor.dna[i]){
          matches++
        }
      }

      const percentMatch = Math.floor(100*matches/pAequor.dna.length)
      console.log(`Specimen ${this.specimenNum} and specimen ${pAequor.specimenNum} have ${percentMatch}% DNA in common`)
    },
    willLikelySurvive() {
      //returns true if at least 60% of DNA is C or G base
      let matches = 0
      for (i=0;i<this.dna.length;i++) {
        if (this.dna[i] == 'C' || this.dna[i] == 'G') {
          matches++
        }
      }
      percent=matches/15
      return percent >=0.6
    }
  };
}


//Build a list of 30 specimens that are likely to survive
pAequorArray = []
let specimenNum = 1
while (pAequorArray.length<30) {
  let newSpecimen = pAequorFactory(specimenNum,mockUpStrand())
    if (newSpecimen.willLikelySurvive()) {
      pAequorArray.push(newSpecimen)
      specimenNum++
    }
}



