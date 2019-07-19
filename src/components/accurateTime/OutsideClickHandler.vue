<template lang="pug">

div(ref="childnode" class="outside-click-container" @mouseover="overModal=true" @mouseout="overModal=false")
	slot(name="modal")

</template>

<script>
export default {
  props: {
    onOutsideClick: {
      type: Function,
      default: () => {}
    },
    focused: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      overModal: false
    }
  },
  methods: {
    onOutsideClickHandler: function(e) {
      if (!this.overModal && this.focused) {
        this.onOutsideClick && this.onOutsideClick()
      }
    }
  },
  mounted() {
    document.addEventListener('click', this.onOutsideClickHandler)
  },
  beforeDestroy() {
    document.removeEventListener('click', this.onOutsideClickHandler)
  }
}
</script>

<style lang="css">
@media screen and (min-width: 768px){
	.outside-click-container {
	  /* width:300px; */
	  /* height : 405px; */
	  position: absolute;
	  opacity: 1;
	  z-index: 2;
		top: -64px;
		right: -272px;
	}
}
@media screen and (max-width: 767px){
	.outside-click-container {
	  width:300px;
	  position: absolute;
	  opacity: 1;
	  z-index: 2;
	  top: 40%;
	  left: 9%;
	}
}
</style>
