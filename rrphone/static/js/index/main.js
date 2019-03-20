Vue.component("heads", {
    template: `
        <ul class="">
            <li v-for="item in lss" class="navbar-nav">
               <a href="#" >{{item}}</a>
            </li>
        </ul>
    `,
    data() {
        return {
            lss: [1, 2, 3, 4, 5, 6],

        }
    },
    methods: {

    }
});





var app = new Vue({
    el: "#app",
    data() {
        return {
            "kaka": [],
            shows: true,
        }
    },
    methods: {
        on_shows: function () {
            this.shows = !this.shows;
        },
        greet: function () {
            this.$http.get('/api/eport/').then(function (res) {
                console.log(res),
                // this.kaka = res.body,
                console.log(this.res)
            }, function (res) {
                console.log(res);
            });
        }
    }
});
