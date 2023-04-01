<script setup lang="ts"></script>

<template>
  <table>
    <div>
      <tr class="flex justify-around">
        <th>Username</th>
        <th>Points</th>
      </tr>
      <hr class="pb-2" />
    </div>
    <div class="space-y-2 pt-2 h-[71vh] flex flex-col overflow-auto">
      <div
        v-for="i in 10"
        :key="i"
        class="flex items-center justify-around align-middle py-4 text-slate-300"
        :class="i % 2 === 0 ? 'bg-slate-500' : 'bg-slate-600'"
      >
        <td>Jorge</td>
        <td>200</td>
      </div>
    </div>
  </table>
</template>
