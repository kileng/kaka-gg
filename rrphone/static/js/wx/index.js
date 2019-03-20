 var mix = new Vue({
        delimiters: ['{[', ']}'],
        el: "#mix",
        data: {
            ts: [],
            see: false,
        },
        methods: {
            // show: function () {
            //     this.show = !this.see;
            // },
            greet: function () {
                this.$http.get('/eport').then(function (res) {
                        console.log(res.body);
                        this.ts = res.body;
                        this.see= !this.see;
                        console.log(this.see);
                }, function () {
                    // console.log('请求失败处理');
                });
            }
        }
    })