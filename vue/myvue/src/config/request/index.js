import axios from "axios";
import { Message } from 'element-ui'

/*
* （1） 数据请求，在请求中添加token
*/
axios.interceptors.request.use(
    req => {
        // 从localStorage中获取token
        var token = localStorage.getItem("token")
        if (token != null) {
            // 将token添加到head中
            req.headers['token'] = token;
        }
        return req;
    },
    err => {
        return Promise.reject(err)
    }
)


/*
* （2） 数据返回，判断token过期
* 返回值格式：{ 'code': "状态码", 'data': "返回值对象", 'msg': "返回值信息" }
* 应用响应状态码：
*             1：获取成功，
*             -1： 获取失败
*
* token状态码：4101：缺少token，4102：token过期，4103：token值错误
*             4104：缺少retoken（刷新token），4105：retoken过期，4106：retoken值错误
*/
// 标志当前是否正在刷洗token
let isNotRefreshing = true;

// 将多个请求放在等待请求队列中
let requests = [];

// 拦截器拦截所有请求
axios.interceptors.response.use(
    async res => {        
        // 判断token过期，刷新token
        if (res.data.code == 4102) {
            console.log("token 过期");

            // 暂存响应配置参数（与请求的配置参数是一样），刷新token后需要使用该参数进行重发
            const tempResConfig = res.config;

            // 判断是否处于刷新阶段
            if (isNotRefreshing) {
                // 当前不处于刷新阶段，进行刷新操作
                // 设置当前处在刷新阶段
                isNotRefreshing = false;

                // 刷新token
                let urlRetoken = "/flask/public/retoken";
                let paramRetoken = { retoken: localStorage.getItem("retoken") };
                return axios.post(urlRetoken, paramRetoken)
                    .then(res => {
                        // 返回值中的retoken缺少、过期、错误，将清除localStorage中的值，并跳转登录
                        if (res.data.code == 4104 || res.data.code == 4105 || res.data.code == 4106) {
                            // 删除本地存储并跳转到登录
                            localStorage.removeItem("token");
                            localStorage.removeItem("retoken");
                            location.href = "/#/login";
                        } else {
                            // 刷新成功之后，将新的token存起来
                            let data = res.data;
                            localStorage.setItem("token", data.data.token);
                            localStorage.setItem("retoken", data.data.retoken);

                            
                            // 执行requests队列中的请求
                            requests.forEach(run => run())
                            // 清空请求队列
                            requests = []

                    
                            // 重新执行未执行成功的请求
                            return axios(tempResConfig);
                        }
                    })
                    .catch(() => {
                        // 请求异常时退回到登录
                        location.href = "/#/login";
                    })
                    .finally(() => {
                        isNotRefreshing = true;
                    })
            } else {
                // 使用Promise对象，将多个请求添加到requests请求队列中，并在刷新token时执行。
                return new Promise(resolve => {
                    requests.push(() => {
                        resolve(axios(tempResConfig));
                    })
                })
            }
        } else {
            // 解析token错误，清空token
            if (res.data.code == 4103) {
                localStorage.removeItem("token");
                localStorage.removeItem("retoken");
                location.href = "/#/login"
            }

            // token为空不做处理
            return res;
        }
    },
    err => {
        // 处理错误
        if (err && err.response && err.response.status) {
            switch (err.response.status) {
                case 404:
                    Message.error('页面未找到')
                    break;
                case 500:
                    Message.error("服务器遇到错误")
                    break;
            }
        }
    }
)
