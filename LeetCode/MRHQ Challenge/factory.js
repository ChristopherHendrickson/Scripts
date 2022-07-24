//object factory
const objectFactory = (objectAttributeOne,objectAttributeTwo) => {
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
        allAttributes() {
           return [this._attributeOne,this._atrributeTwo] 
        }, 
    }
}

