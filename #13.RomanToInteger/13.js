/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const basicSymbols = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  const specicalSymbols = {
    IV: 4,
    IX: 9,
    XL: 40,
    XC: 90,
    CD: 400,
    CM: 900,
  };

  let result = 0;

  for (let i = 0; i < s.length; i++) {
    const currentValue = basicSymbols[s[i]];
    const nextValue = basicSymbols[s[i + 1]];

    for (const symbol in specicalSymbols) {
      if ((currentValue + nextValue).toString().includes(symbol)) {
        s = s.replace(new RegExp(symbol, "g"), specicalSymbols[symbol]);
        result += specicalSymbols[symbol];
      }
    }

    if (nextValue > currentValue) {
      result -= currentValue;
    } else {
      result += currentValue;
    }
  }
  return result;
};
