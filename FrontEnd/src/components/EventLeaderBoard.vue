<script setup lang="ts"></script>

<template>
  <table class="w-full">
    <div class="px-5">
      <tr class="table w-full table-fixed">
        <th>Username</th>
        <th>Points</th>
      </tr>
    </div>
    <div class="space-y-2 pt-2 flex flex-col h-20 overflow-auto">
      <div
        v-for="i in 10"
        :key="i"
        class="flex items-center justify-around align-middle bg-slate-600 mb-2 w-full h-16 rounded-lg text-slate-300"
      >
        <td>Jorge</td>
        <td>200</td>
      </div>
    </div>
  </table>
</template>
