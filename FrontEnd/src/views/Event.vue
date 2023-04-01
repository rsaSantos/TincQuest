<script setup lang="ts">
import { useRoute } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()

enum Tabs {
  info = 'info',
  leaderboard = 'leaderboard',
  questions = 'questions'
}

const openTab = ref(Tabs.info)
const changeTab = (tab: Tabs) => {
  openTab.value = tab
}

console.log(route.params.id)
</script>

<template>
  <div class="bg-slate-700 text-white mx-10 rounded-lg p-4 relative mt-16 min-h-40">
    <img src="@/assets/Images/defaultEventImage.jpg" class="rounded-full w-32 absolute -top-7" />
    <div class="pl-36">
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fugiat, at? Soluta nostrum
      temporibus possimus enim quasi nihil voluptate explicabo unde libero, ipsam officiis animi
      blanditiis magnam nemo saepe, dolorem obcaecati? Lorem ipsum dolor sit amet consectetur
      adipisicing elit. Eligendi delectus sequi, laudantium ea illo dolorum esse odit corrupti
      provident omnis quisquam amet dolore mollitia architecto cupiditate quas qui quidem!
      Similique? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Temporibus accusantium
      iure aperiam ea eligendi nam natus dignissimos sit error, sequi eius voluptatum, minima
      inventore nisi odio molestiae pariatur cumque recusandae! Lorem ipsum dolor sit amet
      consectetur adipisicing elit. Fuga officiis vel corrupti quis necessitatibus eius consequatur
      tempora quae! Quae, tenetur nulla. Dolore a minus deleniti incidunt architecto perspiciatis
      fuga explicabo.
    </div>
    <div class="w-full justify-end flex">
      <button class="bg-white px-2 py-1 rounded-md hover:bg-slate-400 text-black duration-300">
        Join Event
      </button>
    </div>
  </div>
  <div class="pt-5 flex justify-center w-full space-x-4 text-lg text-slate-600">
    <button @click="changeTab(Tabs.info)">Info</button>
    <button @click="changeTab(Tabs.leaderboard)">LeaderBoard</button>
    <button @click="changeTab(Tabs.questions)">Questions</button>
  </div>
  <hr />
</template>
