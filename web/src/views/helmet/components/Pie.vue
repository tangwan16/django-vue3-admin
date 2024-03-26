<template>
    <div>
      <div ref="target" class="w-full h-full"></div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps(['data']);
  
  import { onMounted, ref, watch } from 'vue'
  import * as echarts from 'echarts';
  watch(() => props.data, () => {
    // 渲染 echarts
    renderChart();
});
  // 获取 dom 实例
  const target = ref(null)
  
  // echarts 实例变量
  let mChart = null
  // 在 mounted 生命周期之后，实例化 echarts
  onMounted(() => {
    mChart = echarts.init(target.value);
    // 渲染 echarts
    renderChart();
  });
  
  // 渲染图表
  const renderChart = () => {
  const option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    show:false,
    top: '5%',
    left: 'right',
    orient: 'vertical', // 设置为垂直排列
    textStyle: {
      color: '#64fafb', // 修改字体颜色
      fontSize: 20    // 修改字体大小
    }
  },
  series: [
    {
      name: '人数统计',
      type: 'pie',
      radius: ['50%', '60%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#28458b',
        borderWidth: 2,
        borderRadius: 5, // 修改圆角半径大小
      },
      label: {
        show: false,
        position: 'right',
        formatter: '{b}: {c}'
      },
      emphasis: {
        label: {
          show: false,
          fontSize: 20,
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: props.data.illegalPeople, name: '已戴', itemStyle: { color: '#01f8e8' } },  
        { value: props.data.legalPeople, name: '未戴', itemStyle: { color: '#0a6bff' } }
      ]
    }
  ]
};
    mChart.setOption(option)
  }
  </script>
  <style lang="scss" scoped></style>
  