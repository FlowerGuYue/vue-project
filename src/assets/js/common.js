function search(){}

export default{
  install: function(Vue){
    Vue.prototype.common_search=()=>search()
  }
}
