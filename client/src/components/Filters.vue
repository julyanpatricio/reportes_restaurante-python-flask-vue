<template>
    <div class="container-dataPicker">
      <md-datepicker v-model="dateStart" md-immediately>
        <label>Desde</label>
      </md-datepicker>
      <md-datepicker v-model="dateEnd" md-immediately>
        <label>Hasta</label>
      </md-datepicker>
    </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import format from "date-fns/format";

export default {
  name: 'filters',
  data: () => {
    return {
      dateStart: null,
      dateEnd: null,
    };
  },
  computed: {
    ...mapState(["dateMin", "dateMax"]),
  },
  methods: {
    ...mapActions(["setDateMinSelected","setDateMaxSelected"])
  },
  created(){
    this.dateStart = this.dateMin && new Date(this.dateMin.replaceAll("-", "/"));
    this.dateEnd = this.dateMax && new Date(this.dateMax.replaceAll("-", "/"));
  },
  watch: {
    dateMin: function (newData,oldData) {
      if(newData!==oldData){
      this.dateStart = new Date(this.dateMin.replaceAll("-", "/"));
      }
    },
    dateMax: function (newData,oldData) {
      if(newData!==oldData){
      this.dateEnd = new Date(this.dateMax.replaceAll("-", "/"));
      }
    },
    dateEnd: function (newData,oldData){
      if(newData === null) newData = new Date(this.dateMax.replaceAll("-", "/"))
      if(oldData === null) oldData = new Date()
      if(newData.toDateString() !== oldData.toDateString()){
      this.setDateMaxSelected({'dateMaxSelected':format(newData, "yyyy-MM-dd")})
      }      
    },  
    dateStart: function (newData,oldData){
      if(newData === null) newData = new Date(this.dateMin.replaceAll("-", "/"))
      if(oldData === null) oldData = new Date(null)
      if(newData.toDateString() !== oldData.toDateString()){
      this.setDateMinSelected({'dateMinSelected':format(newData, "yyyy-MM-dd")})
      }
    }
  },
};
</script>

<style scoped>
.container-dataPicker {
  display: flex;
  padding-inline: 30%;
  align-items: center;
}
</style>