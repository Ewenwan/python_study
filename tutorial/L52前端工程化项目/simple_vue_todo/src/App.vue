<template>
  <div id="app">
    <input v-on:keyup.enter="addNewItem" v-model="newItem"/>
    <ul>
      <li v-for="item in items"  v-bind:class={finished:item.isFinished} v-on:click="finish(item)">
        {{item.label}}
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            label: 'read books',
            isFinished: false
          },
          {
            label: 'eat dinner',
            isFinished: true
          }
        ]
      }
    },
    methods: {
      addNewItem () {
        this.items.push({label: this.newItem,isFinished: false})
        this.newItem = ''    //清空输入框
      },
      finish (item) {
        item.isFinished = !item.isFinished
      }
    }
  }
</script>

<style>
  .finished {
    text-decoration: line-through;
  }
</style>
