<template>
  <div class="clock-wrapper">
    <div id="datetime" class="datetime">{{ formattedDate }}&nbsp{{ formattedTime }}</div>
    <div id="weekday" class="weekday">{{ formattedWeekday }}</div>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  data() {
    return {
      formattedDate: '',
      formattedTime: '',
      formattedWeekday: '',
    };
  },
  methods: {
    updateDateTime() {
      const date = moment();
      this.formattedDate = date.format('YYYY.M.D');
      this.formattedTime = date.format('HH:mm');
      this.formattedWeekday = this.getFormattedWeekday(date.day());
      // console.log(this.formattedDate)
      // console.log(this.formattedTime)
      // console.log(this.formattedWeekday)
    },
    getFormattedWeekday(weekday) {
      const weekdays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
      return weekdays[weekday];
    },
  },
  mounted() {
    this.updateDateTime();
    this.clockInterval = setInterval(() => {
      this.updateDateTime();
    }, 1000);
  },
  beforeDestroy() {
    clearInterval(this.clockInterval);
  },
};
</script>


<style>
.clock-wrapper {
  position: relative;
}

.datetime {
  position: absolute;
  top: 60px;
  left: 180px;
  font-size: 20px ;
  line-height: 28px;
  font-weight: 700;
  color: #31C1FD
}

.weekday {
  position: absolute;
  top: 85px;
  left: 380px;
  font-size:  16px;
  line-height: 24px;
  font-weight: 700;
  color: #31C1FD;
}
</style>
