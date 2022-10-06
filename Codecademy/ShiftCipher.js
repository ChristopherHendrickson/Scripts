// Write class below

class ShiftCipher {
  constructor(shift) {
    this.shift = shift
  }

  encrypt(str) {
    str=str.toUpperCase()
    let out=''
    let charCode = 0
    for (let i in str) {
      charCode = str.charCodeAt(i)
      if (charCode >= 65 && charCode <=90){
        charCode += this.shift
        while (charCode > 90) {
          charCode-=26
        }
        
        out += String.fromCharCode(charCode)
      }
    
    
    }
    return out

  }
  decrypt(str) {
    str=str.toLowerCase()
    let out=''
    let code = 0
    for (let i in str) {
      code = str.charCodeAt(i)
      if (code >= 97 && code <=112){
        code -= this.shift
        while (code < 97) {
          code+=26
        }
        
        out += String.fromCharCode(code)
      }
    
    
    }
    return out

  }
}
a = new ShiftCipher(1)
console.log(a.encrypt('abc'))
console.log(a.decrypt('abc'))