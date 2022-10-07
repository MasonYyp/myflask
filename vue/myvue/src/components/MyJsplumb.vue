<template>
  <div class="my_jsplumb">
    <div style="height: 30px;">
      <button v-on:click="htmlGenerateImg()">生成图片</button>
      <button v-on:click="getWidgetInfo()">获取组件信息</button>
    </div>
    <div style="height: 50px; color:red">双击节点、双击连线可以删除！</div>
    <div class="myj_con">
      <draggable class="myjc_left" v-on:end="dragWidget" v-bind="{sort: false}">
        <div v-for="(item, index) in navArr" v-bind:key="index">{{ item }}</div>
      </draggable>

      <div class="myjc_right" v-drag>
        <div class="myjcr_con" v-bind:id="regionId" ref="region">
          <!-- It is betterr not to bind data bidirectional with vue; -->
          <!-- Otherwise, you deleting nodes will cause problems -->
        </div>
      </div> 
    </div>

    <div ref="tempDownloadImg" style="position:absolute; top:0px; height: 22px; font-size: 14px;"></div>

    <div style="position:absolute; top:0px; background-color: #ffffff" v-show="isShowImg">
      <button v-on:click="()=>{isShowImg=false; return false}">关闭</button>
      <img v-bind:src="imgSrc"/>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import { jsPlumb } from "jsplumb";
import html2canvas from "html2canvas"
import canvg from 'canvg';

export default {
  name: "MyJsplumb",
  components: {
    draggable,
  },
  data: function() {
    return {
      regionId: "#region_id",
      plumbIns: null,
      plumbConf: null,
      widgetsInfo: {
        nodes: new Array(),
        lines: new Array()
      },

      navArr: new Array(),
      imgSrc:'',
      isShowImg: false
    };
  },

  directives: {
    // Set drag canvas
    drag: {
      bind(el, binding) {
        if (!binding) {
          return;
        }
        el.onmousedown = (e) => {
          if (e.button == 2) {
            return;
          }
          let disX = e.clientX;
          let disY = e.clientY;
          el.style.cursor = "move";

          document.onmousemove = function(e) {
            el.scrollLeft = el.scrollLeft - (e.clientX - disX);
            disX = e.clientX;
            el.scrollTop = el.scrollTop - (e.clientY - disY);
            disY = e.clientY;
          };

          document.onmouseup = function() {
            el.style.cursor = "auto";
            document.onmousemove = null;
            document.onmouseup = null;
          };
        };
      },
    },
  },

  mounted: function() {
    this.initData();
    this.initJsplumb();
  },

  methods: {
    initData: function() {
      this.navArr = ["河南大学", "软件学院", "Mason"];

      this.widgetsInfo.nodes = [
        {
          id: "con_id_0",
          label: "河南大学",
          top: "100px",
          left: "400px"
        },
        {
          id: "con_id_1",
          label: "软件学院",
          top: "400px",
          left: "500px"
        },
        {
          id: "con_id_2",
          label: "Mason",
          top: "300px",
          left: "200px"
        }
      ];

      this.widgetsInfo.lines=[
        {
          startId: "con_id_0",
          stopId: "con_id_1"
        },
        {
          startId: "con_id_0",
          stopId: "con_id_2"
        }
      ]
    },

    initJsplumb: function() {
      this.$nextTick(() => {
        // Init the jsPlumb
        this.plumbIns = jsPlumb.getInstance();
        this.plumbConf = {
          maxConnections: -1,

          // Not link to oneself
          allowLoopback: false,
          // Set the class of drag
          filter: "drag",
                      
          // Set the type of endpoint
          endpoint: "Dot",
          // Set the style of endpoint
          paintStyle: {
            radius: 4,
            fill: "LightGreen",          
            strokeWidth: 6,
            stroke: "Transparent",
          },
          hoverPaintStyle: {
            radius: 10,
            fill: "Green"
          },

          // Set style of connection line
          connector: 'Bezier',
          // The following styles apply only to type flowchart
          // connector: [ "Flowchart", { gap: 4, alwaysRespectStubs: true }],

          // Set the style of line during drag the line
          connectorStyle: {
            strokeWidth: 2,
            stroke: "LightGreen",
          },
          connectorHoverStyle: {
            strokeWidth: 4,
            stroke: "Green",
          },

          // Set the style of arrow
          connectorOverlays: [["Arrow", { width: 14, length: 14, location: 1 }]]
        };

        // Load the data of jsPlumb
        this.plumbIns.ready(() => {
          this.plumbIns.reset();
          // It is best to set the container
          this.plumbIns.setContainer(this.$refs.region);
          
          // Init the data
          this.widgetsInfo.nodes.forEach((item)=>{
            this.addOneNode(item);
          });

          this.widgetsInfo.lines.forEach((item)=>{
            this.addOneLine(item);
          });

          this.initConnectLine();
        });
      });
    },

    initConnectLine: function(){
      this.plumbIns.bind("connection", (info) => {
        let oneLine = {
          startId: info.sourceId,
          stopId: info.targetId
        }
        this.widgetsInfo.lines.push(oneLine);
        
        console.log("连接成功");
      });

      this.plumbIns.bind("beforeDrop", (info) => {
        if (info.sourceId === info.targetId) {
          console.log("节点不支持连接自己");
          return false;
        }

        if(this.isExitLine(info.sourceId, info.targetId)){
          console.log("连接已存在");
          return false;
        }

        return true;
      });      

      // Delete the connection of node
      this.plumbIns.bind("dblclick", (conn) => {
        this.plumbIns.deleteConnection(conn);
        this.removeOneLine(conn.sourceId, conn.targetId);
        console.log("删除连线");
      });

    },

    // Draw the widget
    dragWidget: function(event) {
      // Get position of widget
      let widgetX = event.originalEvent.clientX;
      let widgetY = event.originalEvent.clientY;
      let regionDom = this.$refs.region;
      let regionRect = regionDom.getBoundingClientRect();

      // Judge the widget in the region
      if (
        widgetX > regionRect.left &&
        widgetX < regionRect.left + regionRect.width &&
        widgetY > regionRect.top &&
        widgetY < regionRect.top + regionRect.height
      ) {
        let uuid = new Date().getTime();
        // Set the parameter
        let curConId = "con_id_" + uuid;
        let left = widgetX - regionRect.left + regionDom.scrollLeft;
        let top = widgetY - regionRect.top + regionDom.scrollTop;

        let oneNode = {
          id: curConId,
          label: event.item.innerText,
          top: top + "px",
          left: left + "px"
        };

        this.widgetsInfo.nodes.push(oneNode);
        this.addOneNode(oneNode);
      } else {
        alert("请拖拽到内容框中");
      }
    },

    // Generate the image with the svg and html
    htmlGenerateImg: function(){
      const htmlDom =  new Promise((resolve)=>{
        let regionDom = this.$refs.region;

        // Solve the problem that html2canvas cant not generate img
        let tempDownloadImg = this.$refs.tempDownloadImg;
        regionDom = tempDownloadImg.appendChild(regionDom.cloneNode(true));

        // Find SVG under current node, with the ':scope'
        var svgArr = regionDom.querySelectorAll(":scope>svg");

        // Convert SVG to img
        svgArr.forEach((node) => {
          const canvas = document.createElement("canvas");
          let svgXml = new XMLSerializer().serializeToString(node);
          canvg(canvas, svgXml);

          canvas.style.zIndex = 9;
          if (node.style.position) {
            canvas.style.position += node.style.position
            canvas.style.left += node.style.left
            canvas.style.top += node.style.top
          }

          // Add the dom in the region
          regionDom.appendChild(canvas)
        });

        return resolve(regionDom);
      });

      const dealImg = async ()=>{
        let data = await htmlDom;
        html2canvas(data, { useCORS: true }).then((canvas) => {          
          // Download image
          const link = document.createElement('a');
           // Convert the canvas to base64
          link.href = canvas.toDataURL('image/png');
          link.setAttribute('download', 'img.png');
          link.style.display = 'none';
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          
          /*
          this.imgSrc = canvas.toDataURL('image/png');
          this.isShowImg = true;
          */

          // Clear the html in the html
          this.$refs.tempDownloadImg.innerHTML="";
          data = null;
          canvas = null;
        }).catch((e) => console.log(e));
      }
      
      // Processing data asynchronously
      dealImg();
    },

    isExitLine: function(startId, stopId){
      let lines = this.widgetsInfo.lines;
      for(let i=0; i<lines.length; i++){
        if((lines[i].startId==startId && lines[i].stopId==stopId)
          ||lines[i].startId==stopId && lines[i].stopId==startId){
          return true;
        }
      }
      return false;
    },

    // Add the node 
    addOneNode: function(oneNode){
      // Notice !!!
      // It is betterr not to bind data bidirectional with vue
      // Otherwise, you deleting nodes will cause problems

      // Add one dom node
      let nodeDom = document.createElement('div');
      nodeDom.id = oneNode.id;
      nodeDom.innerHTML = oneNode.label;

      // The 'type' must be set to work with CSS
      nodeDom.setAttribute("type", "node");
      nodeDom.setAttribute("style", "top:"+oneNode.top+"; left:"+oneNode.left);
      nodeDom.addEventListener("dblclick", ()=>{this.removeOneNode(oneNode.id)});
      document.getElementById(this.regionId).appendChild(nodeDom);

      // Add the anchor of component
      this.plumbIns.makeSource(oneNode.id, { anchors:"Bottom", isSource: true}, this.plumbConf);
      this.plumbIns.makeTarget(oneNode.id, { anchors:"Top", isTarget: true }, this.plumbConf);
            
      this.plumbIns.addEndpoint(oneNode.id, { anchors:"Bottom", isSource: true }, this.plumbConf);
      this.plumbIns.addEndpoint(oneNode.id, { anchors:"Top", isTarget: true }, this.plumbConf);

      // Set drag and the region
      this.plumbIns.draggable(oneNode.id, { containment: this.regionId });
    },

    // Add the line
    addOneLine: function(oneLine){
      // Notice, this is to connect two node
      let connParam = {
        source: oneLine.startId,
        target: oneLine.stopId
      };
      let connStyle = {
        // This parameter must be anchors
        anchors: ['Bottom', 'Top']
      };
      this.plumbIns.connect(connParam, connStyle);
    },

    removeOneNode: function(nodeId) {
      // Remove the line of widgets
      this.widgetsInfo.lines = this.widgetsInfo.lines.filter((line)=>{
        return (line.startId != nodeId && line.stopId != nodeId)
      });
      // Remove the node of widgets
      this.widgetsInfo.nodes = this.widgetsInfo.nodes.filter((node)=>{
        return node.id != nodeId;
      });

      // Remove the dom node 
      this.plumbIns.remove(nodeId);
      this.plumbIns.removeAllEndpoints(nodeId);
      this.plumbIns.deleteConnectionsForElement(nodeId);
    },

    removeOneLine: function(startId, stopId) {
      for(let i=0; i<this.widgetsInfo.lines.length; i++){
        let line = this.widgetsInfo.lines[i];
        if(line.startId == startId && line.stopId == stopId){
          this.widgetsInfo.lines.splice(i, 1);
          return;
        }
      }
    },

    getWidgetInfo: function(){
      console.log(this.widgetsInfo);
    }
  },

  destroyed: function(){
    this.plumbIns.reset();
    this.plumbIns = null;
  }
};
</script>

<style scoped>
.my_jsplumb {
  position: relative;
}

.my_jsplumb > div {
  position: relative;
}

.myj_con {
  display: flex;
}

.myjc_left {
  width: 200px;
  height: 600px;
  position: relative;
}
.myjc_left > div {
  width: 100%;
  height: 40px;
  line-height: 40px;
  margin: 8px 0px;
  background-color: #ebeef5;
  cursor: pointer;
}

.myjc_right {
  flex: 1;
  border: solid 1px #e6a23c;
  overflow: scroll;
  height: 600px;
  width: 100%;
  position: relative;
}

.myjc_right::-webkit-scrollbar {
  width: 4px;
  height: 4px;
}

.myjc_right::-webkit-scrollbar-thumb {
  border-radius: 4px;
  background: #e0e3e7;
  height: 20px;
}

.myjc_right::-webkit-scrollbar-track {
  background-color: transparent;
}

.myjcr_con{
  width: 2000px;
  height: 900px;
  position: relative;
}

.myjcr_con>>> div[type="node"] {
  min-width: 100px;
  height: 22px;
  font-size: 14px;
  position: absolute;
  padding: 8px 10px;
  display: inline-block;
  border-radius: 8px;
  cursor: pointer;
  background-color: #ebeef5;
}

</style>
