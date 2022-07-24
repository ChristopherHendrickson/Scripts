//object factory
const createObject = (objectAttributeOne,objectAttributeTwo) => {
    return {
        _attributeOne : objectAttributeOne,
        _atrributeTwo : objectAttributeTwo,
        
        set attributeOne(newAttribute) {
            this._attributeOne = newAttribute
        },
        set attributeTwo(newAttribute) {
            this._atrributeTwo = newAttribute
        },
        get attributeOne() {
            return this._attributeOne
        },
        get attributeTwo() {
            return this._attributeTwo
        },
        get allAttributes() {
           return [this._attributeOne,this._atrributeTwo] 
        }, 
    }
}

const newObject = createObject(1,2)
const newObject2 = createObject('Jane','Doe')
console.log(newObject.allAttributes)
console.log(newObject2.attributeOne)
newObject.attributeOne = 'string'
console.log(newObject.allAttributes)
