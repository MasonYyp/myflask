(function(t){function n(n){for(var r,c,a=n[0],i=n[1],f=n[2],p=0,s=[];p<a.length;p++)c=a[p],Object.prototype.hasOwnProperty.call(o,c)&&o[c]&&s.push(o[c][0]),o[c]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(t[r]=i[r]);l&&l(n);while(s.length)s.shift()();return u.push.apply(u,f||[]),e()}function e(){for(var t,n=0;n<u.length;n++){for(var e=u[n],r=!0,a=1;a<e.length;a++){var i=e[a];0!==o[i]&&(r=!1)}r&&(u.splice(n--,1),t=c(c.s=e[0]))}return t}var r={},o={app:0},u=[];function c(n){if(r[n])return r[n].exports;var e=r[n]={i:n,l:!1,exports:{}};return t[n].call(e.exports,e,e.exports,c),e.l=!0,e.exports}c.m=t,c.c=r,c.d=function(t,n,e){c.o(t,n)||Object.defineProperty(t,n,{enumerable:!0,get:e})},c.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},c.t=function(t,n){if(1&n&&(t=c(t)),8&n)return t;if(4&n&&"object"===typeof t&&t&&t.__esModule)return t;var e=Object.create(null);if(c.r(e),Object.defineProperty(e,"default",{enumerable:!0,value:t}),2&n&&"string"!=typeof t)for(var r in t)c.d(e,r,function(n){return t[n]}.bind(null,r));return e},c.n=function(t){var n=t&&t.__esModule?function(){return t["default"]}:function(){return t};return c.d(n,"a",n),n},c.o=function(t,n){return Object.prototype.hasOwnProperty.call(t,n)},c.p="";var a=window["webpackJsonp"]=window["webpackJsonp"]||[],i=a.push.bind(a);a.push=n,a=a.slice();for(var f=0;f<a.length;f++)n(a[f]);var l=i;u.push([0,"chunk-vendors"]),e()})({0:function(t,n,e){t.exports=e("56d7")},"034f":function(t,n,e){"use strict";e("64a9")},"56d7":function(t,n,e){"use strict";e.r(n);e("cadf"),e("551c"),e("f751"),e("097d");var r=e("2b0e"),o=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{attrs:{id:"app"}},[e("div",[e("button",{on:{click:function(n){return t.getdata()}}},[t._v("登录")]),e("img",{attrs:{src:t.imgSrc}})])])},u=[],c=e("bc3a"),a=e.n(c),i={name:"app",data:function(){return{imgSrc:e("cf05")}},methods:{getdata:function(){a.a.get("/task/login").then((function(t){console.log(t.data)}))}}},f=i,l=(e("034f"),e("2877")),p=Object(l["a"])(f,o,u,!1,null,null,null),s=p.exports;r["a"].config.productionTip=!1,new r["a"]({render:function(t){return t(s)}}).$mount("#app")},"64a9":function(t,n,e){},cf05:function(t,n,e){t.exports=e.p+"img/logo.82b9c7a5.png"}});
//# sourceMappingURL=app.ad4bcb1d.js.map