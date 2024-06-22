# Installing Node.js to run JavaScript
```bash
sudo apt update && sudo apt install nodejs -y  # install nodejs on debian based system
node -v                                        # after installation, check version
sudo apt install npm -y                        # install nodejs package manager
npm -v                                         # after installation, check version
```
- Create JavaScript file named *.js

#### Example JavaScript file named "Addition.js":
```js
// Function to add two variables.
 const add = (a, b) => {
    return a + b
}
 
console.log(add(4, 6))
```
#### Run JavaScript file in a Terminal:
```bash
node Addition.js
```
#### References: 
- https://www.geeksforgeeks.org/installation-of-node-js-on-linux/?ref=lbp
- https://www.geeksforgeeks.org/how-do-you-run-javascript-script-through-the-terminal/

# Run JavaScript directly in the Terminal
```bash
notroot@Test:~$ node
Welcome to Node.js v12.22.9.
Type ".help" for more information.
> 
> process.exit()
```

# Remove JavaScript Execution
#### Notes: 
- put the message in 'console.log( )'
- The log() method writes a message (logs) to the console. This method is useful for testing purposes.
```js
console.log(message)
```
#### References: 
- https://youtu.be/bKRNH8vO67g?t=1252
- https://www.w3schools.com/jsref/met_console_log.asp
- http://www.schillmania.com/content/entries/2009/javascript-malware-obfuscation-analysis/
- http://isc.sans.org/diary.html?storyid=4246

# Obfuscated Code
same code from [Addition.js](https://github.com/ciwen3/JH-Notes/blob/main/JavaScript.md####example-javascript-file-named-"addition.js":) put through https://obfuscator.io/
```js
function _0x5707(_0x35adf1,_0x23e040){const _0x556da3=_0x556d();return _0x5707=function(_0x5707ab,_0x13eef2){_0x5707ab=_0x5707ab-0x91;let _0x2851af=_0x556da3[_0x5707ab];return _0x2851af;},_0x5707(_0x35adf1,_0x23e040);}const _0x20950b=_0x5707;(function(_0x10f8e4,_0x167f31){const _0x55358c=_0x5707,_0x5efefb=_0x10f8e4();while(!![]){try{const _0x38b04e=parseInt(_0x55358c(0x98))/0x1+-parseInt(_0x55358c(0x95))/0x2+parseInt(_0x55358c(0x93))/0x3+parseInt(_0x55358c(0x97))/0x4+parseInt(_0x55358c(0x92))/0x5+parseInt(_0x55358c(0x99))/0x6+-parseInt(_0x55358c(0x94))/0x7*(parseInt(_0x55358c(0x96))/0x8);if(_0x38b04e===_0x167f31)break;else _0x5efefb['push'](_0x5efefb['shift']());}catch(_0x2cb98e){_0x5efefb['push'](_0x5efefb['shift']());}}}(_0x556d,0xaddaa));const add=(_0x2adf5d,_0x220486)=>{return _0x2adf5d+_0x220486;};console[_0x20950b(0x91)](add(0x4,0x6));function _0x556d(){const _0x19e2da=['5672435QNUTIW','1336176aQfnHN','3721186kHPsOX','1931438evbblN','24vDtuHv','556832FPLZdT','1320936ZxjwXY','1395576DbBnFv','log'];_0x556d=function(){return _0x19e2da;};return _0x556d();}
```



# Code Beautifier
Same [Obfuscated Code](https://github.com/ciwen3/JH-Notes/blob/main/JavaScript.md#obfuscated-code) as above put through https://beautifier.io/
```js
function _0x5707(_0x35adf1, _0x23e040) {
    const _0x556da3 = _0x556d();
    return _0x5707 = function(_0x5707ab, _0x13eef2) {
        _0x5707ab = _0x5707ab - 0x91;
        let _0x2851af = _0x556da3[_0x5707ab];
        return _0x2851af;
    }, _0x5707(_0x35adf1, _0x23e040);
}
const _0x20950b = _0x5707;
(function(_0x10f8e4, _0x167f31) {
    const _0x55358c = _0x5707,
        _0x5efefb = _0x10f8e4();
    while (!![]) {
        try {
            const _0x38b04e = parseInt(_0x55358c(0x98)) / 0x1 + -parseInt(_0x55358c(0x95)) / 0x2 + parseInt(_0x55358c(0x93)) / 0x3 + parseInt(_0x55358c(0x97)) / 0x4 + parseInt(_0x55358c(0x92)) / 0x5 + parseInt(_0x55358c(0x99)) / 0x6 + -parseInt(_0x55358c(0x94)) / 0x7 * (parseInt(_0x55358c(0x96)) / 0x8);
            if (_0x38b04e === _0x167f31) break;
            else _0x5efefb['push'](_0x5efefb['shift']());
        } catch (_0x2cb98e) {
            _0x5efefb['push'](_0x5efefb['shift']());
        }
    }
}(_0x556d, 0xaddaa));
const add = (_0x2adf5d, _0x220486) => {
    return _0x2adf5d + _0x220486;
};
console[_0x20950b(0x91)](add(0x4, 0x6));

function _0x556d() {
    const _0x19e2da = ['5672435QNUTIW', '1336176aQfnHN', '3721186kHPsOX', '1931438evbblN', '24vDtuHv', '556832FPLZdT', '1320936ZxjwXY', '1395576DbBnFv', 'log'];
    _0x556d = function() {
        return _0x19e2da;
    };
    return _0x556d();
}
```
