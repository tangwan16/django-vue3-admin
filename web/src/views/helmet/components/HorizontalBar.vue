<template>
  <div>
    <div ref="target" class="w-full h-full"></div>
  </div>
</template>

<script setup>
import * as echarts from 'echarts';
import { onMounted, ref, watch } from 'vue'
const props = defineProps(['data']);
watch(() => props.data, () => {
    renderChart();
});

// 获取 dom 实例
const target = ref(null)
let mChart = null
// 在 mounted 生命周期之后，实例化 echarts
onMounted(() => {
  mChart = echarts.init(target.value);
});
// 渲染图表
const renderChart = () => {
  const option = {
    tooltip: {},
    xAxis: {
      type: 'category',
      axisLine: { show: false },
      data: props.data.map((item) => item.name),
    },
    yAxis: {
      type: 'value',
      axisLine: {
        show: false,
      },
      splitLine: {
      lineStyle: {
        color: '#1a467d'  // y轴分隔线颜色
      }
    }
    },
    grid: {
      top: 50,
      right: 0,
      bottom: 0,
      left: 0,
      // 计算边距时，包含标签
      containLabel: true,
    },
    series: [
      {
        name: '数量',
        type: 'bar',
        data: props.data.map(item => ({
          name: item.name,
          value: item.value
        })),
        // 轴宽度
        barWidth: 24,

        itemStyle: {
          //使用渐变色
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#09cac5' },  // 渐变色起始颜色
            { offset: 1, color: '#003490' }   // 渐变色结束颜色
          ]),
          barBorderRadius: 4, // 设置柱子的圆角
          shadowColor: 'rgba(0, 0, 0, 0.3)', // 设置柱子的阴影颜色
          shadowBlur: 5 // 设置柱子的阴影模糊大小
        },
      }
    ]
  }
  mChart.setOption(option)
}
</script>
<style lang="scss" scoped></style>
