Vue.component("bubu",{
	delimiters: ['{[', ']}'],
	template:`
		<div>
			<h1>使用方法</h1>
		
		
			<h3>请将要播放的网址直接放到下边的输入框</h3>
		
		
			<form class="form-group">
				<input v-model.lazy="re" class="form-control">
				<iframe :src=rr+re  allowfullscreen="ture" border="0" marginwidth="0" marginheight="0" scrolling="no" width="100%" height="600px" frameborder="0">
				</iframe>
			</form>
		</div>
	`,
	data(){
		return{
		    rr:"http://api.xfsub.com/index.php?url=",
            re:null
		}
	}
})




new Vue({
    el:"#kaka",
    delimiters: ['{[', ']}'],
})




