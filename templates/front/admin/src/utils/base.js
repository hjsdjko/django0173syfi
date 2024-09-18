const base = {
    get() {
        return {
            url : "http://localhost:8080/django0173syfi/",
            name: "django0173syfi",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于大数据技术的智慧居家养老服务平台"
        } 
    }
}
export default base
