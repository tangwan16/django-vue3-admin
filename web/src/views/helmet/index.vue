<template>
	  <div class="bg-[url('helmet/assets/imgs/bg.png')] bg-cover bg-center bg-no-repeat 
  h-screen overflow-hidden">
	  <!-- 时间显示组件-->
	  <Clock />
	  <div class=" relative bg-[url('helmet/assets/imgs/top.png')] bg-cover bg-center p-0 h-head flex justify-center">
      <p class=" text-white text-5xl relative top-5">数据可视化平台</p>
    </div>
	  <!-- 下 -->
	  <div class="flex">
		<!-- 左 -->
		<div>

		  <!-- 项目简介 -->
		  <div class="  bg-[url('helmet/assets/imgs/intro.png')] bg-cover bg-top h-70 ml-10">
			<div class="pt-12">
				<p class="text-white text-center text-base">
				本套监管系统使用人工智能算法进行图像识别，<br>
 				 致力于解决现场施工的工人安全帽佩戴监管效率低下等问题，<br>
 			 	一旦识别到未佩戴安全帽的工人，<br>
  				系统会自动报警并储存报警相关信息，<br>
  				可在系统内查询报警记录及图片证据。
				</p>
			</div>
		  </div>




		  <!-- 今日各组违规统计 -->
		  <div class="bg-[url('helmet/assets/imgs/daliyVio.png')] bg-cover bg-top h-80 mt-10 ml-10">
			<div class="flex w-full h-1/5 ">
			</div>
			<div class=" flex justify-center items-center h-4/5 ">
			  <HorizontalBar class="w-full h-full box-border" :data="groupedCounts" />
			</div>
		  </div>

		  <!-- 今日安全帽佩戴概况 -->
		  <div class="flex flex-col bg-[url('helmet/assets/imgs/DaliyHelmet.png')] bg-cover bg-top h-60  mt-12 ml-10">

			<div class="flex w-full h-1/5 ">
			</div>

			<div class=" flex h-4/5 w-full ">
			  <div class=" flex flex-col h-full  items-center justify-center w-1/3">
				<div class="text-fontblue text-2xl">{{ legalPeople }}</div>
				<div class="text-white text-xl mb-2">未戴</div>
			  </div>
			  <div class=" flex flex-col items-center justify-center relative h-full w-1/3 ">
				<p id="PieNum" class="text-fontpieinnner text-xl z-10 ">{{ totalPeople }}</p>
				<p id="PieChar" class="text-fontpieinnner text-xl z-10 ">在岗总数</p>
				<img src="helmet/assets/imgs/pie.png" class="absolute" />
				<Pie class="h-56 w-96 box-border absolute" :data="chartData" />
			  </div>
			  <div class="flex flex-col h-full w-1/3 items-center justify-center">
				<p class="text-fontblue text-2xl" ref="animatedNumber">{{ tweened.illegalPeople.toFixed(0) }}</p>
				<p class="text-white text-xl ">已戴</p>
			  </div>
			</div>

			
		  </div>
		</div>

		<!-- 右 -->
		<div class="w-1/4 flex flex-col flex-1 p-0 m-0">
		  <!-- 右上 -->
		  <div class="flex h-72 items-center">
			<template v-for="index in [1,2,3]">
				<div class="flex flex-col w-1/3">
					<BorderBox1 class="container w-1/3 bg-[url('helmet/assets/imgs/monitor.png')] bg-center bg-no-repeat"  
					:style="{
						width: '340px',
						height: '210px',
						left: '50px',}">
						
						<div class="h-1/4 pt-7 pl-5">
							<p class="text-white text-left text-base">
								第{{selectedVideoIndexes[index]}}通路
							</p>
						</div>
						<div class="h-36 w-full">
						<video :src="currentVideoIndexes[index]" class="w-auto rounded h-full mx-auto" muted autoplay loop
							ref="videoPlayer"></video>
						</div>
					</BorderBox1>

					<div class="flex items-center justify-center mt-2 pr-12">
						<p class=" text-white text-xl block">
						 监控#{{selectedVideoIndexes[index]}} <!-- 显示文字 -->
						</p>
					</div>
				</div>
			</template>
		  </div>

		  <!-- 右中 -->
		  <div class="flex bg-[url('helmet/assets/imgs/tunnel.png')] bg-no-repeat bg-center bg-contain h-96 relative">
			
			<template v-for="item in 6" :key="item">
				<div  class="flex">
					<img
						src='helmet/assets/imgs/monitor_icon.png' 
						@click="playVideo(item)"
						class="absolute h-auto w-auto"
						:style="{
							left: 280 + 150 * (item - 1)+'px',
							top: '80px',
							transform:selectedVideoIndexes[ Math.floor((item+1)/2)] === item ? 'scale(1.5)' : 'scale(1)',
							transition: 'transform 1s ease',
							opacity: selectedVideoIndexes[ Math.floor((item+1)/2)] === item ? '1' : '0.5',
							cursor: 'pointer',
						}"
					/>
					<div
						v-if="selectedVideoIndexes[ Math.floor((item+1)/2)] ===item"
						class="absolute h-auto w-auto text-white text-base"
						:style="{
						left: 270 + 150 * (item - 1)+'px',
						top: '110px',
						transition: 'transform 1s ease',
						}"
					>
						监控{{selectedVideoIndexes[ Math.floor((item+1)/2)]}}
					</div>
				</div>
			</template>

			<template v-for="person in totalInformation" :key="person.id">
				<div class="absolute" :style="calculatePosition(person)">
					<img v-if="person.illegal === 'yes'" src="helmet/assets/imgs/red.png" class="h-auto w-auto">
            		<img v-else src="helmet/assets/imgs/green.png" class="h-auto w-auto">
				</div>
			</template>

		</div>

		  <!-- 右下 -->
		  <div
			class="flex flex-col bg-[url('helmet/assets/imgs/VioPerson.png')] bg-no-repeat bg-center h-60 px-16  bg-contain overflow-hidden">
			<div class="h-1/3 w-full">
			</div>
			<div class="h-2/3 w-full ">
			  <Violators :data="totalInformation" />
			</div>
		  </div>
		</div>
	  </div>
	</div>
  </template>
  
  <script setup>
  import { ref, watch,  onMounted} from 'vue'
  import Clock from './components/Clock.vue'
  import HorizontalBar from './components/HorizontalBar.vue'
  import Pie from './components/Pie.vue'
  import Violators from './components/Violators.vue';
  
  import { updateTotalInfo } from './totalinformation';
  import { updateUWB } from './uwb';
  import { getTotalInfo } from './totalinformation';
  import { BorderBox1 } from '@dataview/datav-vue3';
  import gsap from 'gsap'

  
  const totalInformation = ref(null)
  

  //每组未带安全帽的人数
  const groupedCounts = ref([]);
  //总人数
  const totalPeople = ref(11);
  const illegalPeople = ref(10);
  const legalPeople = ref(1);
  //表格数据
  const chartData = ref({
	  totalPeople: 11,
	  illegalPeople: 10,
	  legalPeople: 1
  });
  const videoPlayer = ref(null);
  const currentVideo_1 = ref("");
  const currentVideo_2 = ref("");
  const currentVideo_3 = ref("");

  const selectedVideoIndex_1 = ref(null);
  const selectedVideoIndex_2 = ref(null);
  const selectedVideoIndex_3 = ref(null);
  
  const selectedVideoIndexes = ref({
      1: selectedVideoIndex_1,
      2: selectedVideoIndex_2,
      3: selectedVideoIndex_3
    });

const currentVideoIndexes =ref({
	1: currentVideo_1,
    2: currentVideo_2,
    3: currentVideo_3
});

  
  
  const loadData = async () => {
	  const updateUWBRes =await updateUWB();
	  if(updateUWBRes.data.code===1){
		console.log("更新UWB成功")
	  }
	  else console.log("更新UWB失败")
  
	  const updateTotalInfoRes = await updateTotalInfo();
	  if(updateTotalInfoRes.data.code===1){
		console.log("更新TotalInfo成功")
	  }
	  else console.log("更新TotalInfo失败")
	  console.log("TotalInfo的数据是:")
	  const getTotalInfoRes= await getTotalInfo()
	  totalInformation.value = getTotalInfoRes.data.data;
	  console.log(totalInformation.value);

  };
  
  onMounted (()=>loadData())
  
//   setInterval(() => {
//   	loadData()
//   }, 3000)
  
  
  // totalInformation 一变化更新chartData数据
  watch(totalInformation, (newValue) => {
	  const peopleWithIllegalYes = newValue.filter(person => person.illegal === 'yes');
  
	  chartData.value = {
		totalPeople: newValue.length,
		illegalPeople: peopleWithIllegalYes.length,
		legalPeople:totalPeople.value - illegalPeople.value
	  };
  
	  // 更新每组中未带安全帽的人数
	  const groupOrder = ['一组', '二组', '三组', '四组', '五组'];
	  const result = groupOrder.map(group => ({ name: group, value: peopleWithIllegalYes.filter(person => person.work_group === group).length }));
	  groupedCounts.value = result;
	  console.log(groupedCounts)
  });
  
  const tweened = ref({ illegalPeople: 10, totalPeople: 11 });
  
  
  //当illegalPeople, totalPeople变化动态化显示
  watch([illegalPeople, totalPeople],() => {
	  gsap.to(tweened.value, 
	  { duration: 0.5,
		illegalPeople: Number(illegalPeople.value) || 0, 
		totalPeople: Number(totalPeople.value) || 0, 
		onUpdate: updateNumber }); //调用updateNumber回调函数
	}
  );
  
  const updateNumber = () => {
	// 更新数字显示
	const illegalNumberElement = document.querySelector('.text-fontblue');
	if (illegalNumberElement) {
	  illegalNumberElement.textContent = tweened.value.illegalPeople.toFixed(0);
	}
  
	const totalNumberElement = document.querySelector('.text-fontpieinnner');
	if (totalNumberElement) {
	  totalNumberElement.textContent = tweened.value.totalPeople.toFixed(0);
	}
  };
  
  
//uwb计算人员位置   
  const calculatePosition = (person) => {
	const left = (person.x / 100) * (1000 - 200) + 200;
	const top = (person.y / 50) * (270 - 170) + 170;
	return {
	  left: `${left}px`,
	  top: `${top}px`
	};
  };

	//更新摄像头   
  const playVideo = (videoNumber) => {
	if (videoNumber === 1) {
	  currentVideo_1.value = "helmet/flask/video_1.mp4";
	  selectedVideoIndex_1.value = 1;
	} else if (videoNumber === 2) {
	  currentVideo_1.value = "helmet/flask/video_2.mp4";
	  selectedVideoIndex_1.value = 2;
	} else if (videoNumber === 3) {
	  currentVideo_2.value = "helmet/flask/video_3.mp4";
	  selectedVideoIndex_2.value = 3;
	} else if (videoNumber === 4) {
	  currentVideo_2.value = "helmet/flask/video_4.mp4";
	  selectedVideoIndex_2.value = 4;
	} else if (videoNumber === 5) {
	  currentVideo_3.value = "helmet/flask/video_5.mp4";
	  selectedVideoIndex_3.value = 5;
	} else if (videoNumber === 6) {
	  currentVideo_3.value = "helmet/flask/video_6.mp4";
	  selectedVideoIndex_3.value = 6;
	}
	// videoPlayer.value.play();
	videoPlayer.play();
  };
  


  </script>
  <style scoped>
#temp {
	position: absolute;
	z-index: 2;
	width: auto;
	height: auto;
}

#PieNum {
	left: 195px;
}

#PieChar {
	left: 173px;
}

.intro-background {
  background-image: url('helmet//assets/imgs/intro.png');
  background-size: cover;
  background-position: center;
}

.intro-div{
	width: 83.333333%;
  margin: 0;
  height: 80%;
  text-align: center;
  padding-left: 2%;
  margin-left: 10%;
}

.intro-content {
	color: white;
	text-align: left;
	font-size:  16px;
	line-height: 24px;
}
  </style>
  
