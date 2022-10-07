<template>
  <div>
    <div>
      <input type="button" value="放大" v-on:click="zoomIn" />
      <input type="button" value="缩小" v-on:click="zoomOut" />
    </div>
    <div id="jsmind_container"></div>
  </div>
</template>

<script>
import "jsmind/style/jsmind.css";
import jsMind from "jsmind/js/jsmind.js";
window.jsMind = jsMind;

require("jsmind/js/jsmind.draggable.js");
require("jsmind/js/jsmind.screenshot.js");
require("@/assets/js/jsmind.menu.js");

export default {
  name: "MyJsmind",

  data: function () {
    return {
      jm: null,
    };
  },

  mounted: function () {
    this.init_data();
  },

  methods: {
    init_data: function () {
      var mind = {
        /* 元数据，定义思维导图的名称、作者、版本等信息 */
        meta: {
          name: "jsMind-demo-tree",
          author: "hizzgdev@163.com",
          version: "0.2",
        },
        /* 数据格式声明 */
        format: "node_tree",
        /* 数据内容 */
        data: {
          id: "root",
          topic: "jsMind",
          children: [
            {
              id: "easy",
              topic: "Easy",
              direction: "left",
              expanded: false,
              children: [
                { id: "easy1", topic: "Easy to show" },
                { id: "easy2", topic: "Easy to edit" },
                { id: "easy3", topic: "Easy to store" },
                { id: "easy4", topic: "Easy to embed" },
              ],
            },
            {
              id: "open",
              topic: "Open Source",
              direction: "right",
              expanded: true,
              children: [
                { id: "open1", topic: "on GitHub" },
                { id: "open2", topic: "BSD License" },
              ],
            },
            {
              id: "powerful",
              topic: "Powerful",
              direction: "right",
              children: [
                { id: "powerful1", topic: "Base on Javascript" },
                { id: "powerful2", topic: "Base on HTML5" },
                { id: "powerful3", topic: "Depends on you" },
              ],
            },
            {
              id: "other",
              topic: "test node",
              direction: "left",
              children: [
                { id: "other1", topic: "I'm from local variable" },
                { id: "other2", topic: "I can do everything" },
              ],
            },
          ],
        },
      };

      var options = {
        container: "jsmind_container",
        editable: true,
        theme: "primary",

        menuOpts: {
          showMenu: true,
          injectionList: [
            {
              target: "edit",
              text: "编辑节点",
              callback: function (node) {
                console.log(node);
              },
            },
            {
              target: "addChild",
              text: "添加子节点",
              callback: function (node) {
                console.log(node);
              },
            },
            {
              target: "addBrother",
              text: "添加兄弟节点",
              callback: function (node) {
                console.log(node);
              },
            },
            {
              target: "delete",
              text: "删除节点",
              callback: function (node) {
                console.log(node);
              },
            },
            {
              target: "screenshot",
              text: "下载导图",
              callback: function (node) {
                console.log(node);
              },
            },
            {
              target: "showAll",
              text: "展开全部节点",
              callback: function (node) {
                console.log(node);
              },
            },
            {
              target: "hideAll",
              text: "收起全部节点",
              callback: function (node) {
                console.log(node);
              },
            },
          ],
        },
      };

      this.jm = new jsMind(options);
      this.jm.show(mind);
    },

    zoomIn: function () {
      this.jm.view.zoomIn();
    },

    zoomOut: function () {
      this.jm.view.zoomOut();
    },
  },
};
</script>

<style scoped>
#jsmind_container {
  width: 100%;
  height: 800px;
}
</style>
