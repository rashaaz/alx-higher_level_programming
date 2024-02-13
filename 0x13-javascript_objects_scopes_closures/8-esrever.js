#!/usr/bin/node
exports.esrever = function (list) {
  let ll = list.length - 1;
  let ii = 0;
  while ((ll - ii) > 0) {
    const s = list[ll];
    list[ll] = list[ii];
    list[ii] = s;
    ii++;
    ll--;
  }
  return list;
};
