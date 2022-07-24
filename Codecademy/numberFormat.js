const formatNumber = number => {
  const strNumber = number.toString().split('.');
  strNumber.push('00')
  const reversed = strNumber[0].split('').reverse()
  for (let i=3;i<reversed.length;i+=4) {
    reversed.splice(i,0,',')
  }
  let formatted = reversed.reverse()
  formatted=[formatted.join('')]
  const formattedWithDP = [formatted,strNumber[1]].join('.')
  return formattedWithDP
}