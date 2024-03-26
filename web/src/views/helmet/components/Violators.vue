<template>
  <div>

    <transition name="enlarge-fade">
      <div v-if="isCardClicked" class="overlay" @click="closeModal">
        <div class="modal" @click.stop>
          <div class="enlarged-card">
            <div class="flex h-80 w-120 bg-[url('helmet/assets/imgs/personbg_big.png')] bg-contain bg-no-repeat bg-center items-center">
              <div class="flex items-center justify-center w-1/2">
                <!-- <img class="object-center h-32 w-auto" :src="`./images/${card.path}`" /> -->
              </div>
              <div class="w-1/2">
                <p class="text-2xl text-fontblue">{{ clickedCardData.name }}</p>
                <p class="text-base text-white pt-3">{{ clickedCardData.work_group }}</p>
                <p class="text-base text-white pt-2">{{ clickedCardData.id }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <vue3-seamless-scroll :list="filteredCardList" :direction="'left'" :hover="true" class="overflow-hidden">
      <ul class="list-none p-0 m-0 flex">
        <li v-for="(card, index) in filteredCardList" :key="index"
          class="flex h-44 w-80 bg-[url('helmet/assets/imgs/personbg_big.png')] 
          bg-contain bg-no-repeat bg-center items-center"
          @click="handleCardClick(card)" style="cursor: pointer;">
          <div class="flex items-center justify-center w-1/2">
            <img class="object-center h-32 w-auto" :src= "`./img/${card.path}`" />
          </div>
          <div class="w-1/2">
            <p class="text-2xl text-fontblue">{{ card.name }}</p>
            <p class="text-base text-white pt-3">{{ card.work_group }}</p>
            <p class="text-base text-white pt-2">{{ card.id }}</p>
          </div>
        </li>
      </ul>
    </vue3-seamless-scroll>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { Vue3SeamlessScroll } from "vue3-seamless-scroll";

const props = defineProps(['data']);
const filteredCardList = ref([]);
const isCardClicked = ref(false);
const clickedCardData = ref(null);

watch(() => props.data, () => {
  filteredCardList.value = props.data.filter(person => person.illegal === 'yes');
  filteredCardList.value.forEach(person => {
    // 提取文件名
    const segments = person.path.split('/');
    person.path = segments[segments.length - 1];
  });
});

const handleCardClick = (card) => {
  // 设置被点击的任务卡片的数据，并展示放大效果和背景蒙版
  clickedCardData.value = card;
  isCardClicked.value = true;
};

const closeModal = () => {
  // 关闭模态框，加入 setTimeout 来确保 isCardClicked 更新后再执行关闭
  setTimeout(() => {
    isCardClicked.value = false;
  }, 0);
};
const getImagePath = (path)=> {
      // 拆分路径，提取文件名或文件夹名
      const segments = path.split('/');
      const imgFileName = segments[segments.length - 1]; 
      // 获取文件名或文件夹名
      // 构建完整的图片路径
      return   `@/img/${imgFileName}`
    }
</script>

<style scoped>
/* 添加样式，用于背景蒙版和放大效果 */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(5px); /* 添加虚化效果，10px 是模糊程度，可以根据需要调整 */
  background: rgba(0, 0, 0, 0.5);
  /* 半透明黑色背景 */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.modal {
  background: rgba(0, 0, 0, 0); /* 半透明黑色背景 */
  padding: 20px;
  border-radius: 5px;
}
/* 添加过渡效果的样式 */
.enlarge-fade-enter-active, .enlarge-fade-leave-active {
  transition: opacity 0.5s;
}
.enlarge-fade-enter, .enlarge-fade-leave-to {
  opacity: 0;
}
.enlarged-card {
  /* 根据需要设置放大卡片的样式 */
  width: 500px;
  height: 300px;
}
</style>
  