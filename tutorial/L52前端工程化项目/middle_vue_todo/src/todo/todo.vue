<template>
    <section class="real-app">
        <input type="text" class="add-input" autofocus="autofocus" placeholder="接下去要做什么" @keyup.enter="addTodo"/>
        <Item v-for="todo in filteredTodos" :todo="todo" :key="todo.id" @del="deleteTodo"></Item>
        <Tabs :filter="filter" :todos="todos" @toggle="toggleFilter" @clearAllCompleted="clearAllCompleted"></Tabs>
    </section>
</template>

<script>
    import Item from './item.vue'
    import Tabs from './tabs.vue'

    let id = 0

    export default {
        name: "todo",
        data(){
            return {
                todos: [],
                filter: 'all'
            }
        },
        components: {
            Item,
            Tabs
        },
        computed: {
            filteredTodos() {
                if (this.filter === 'all') {
                    return this.todos
                }
                const completed = this.filter === 'completed'
                return this.todos.filter(todo => todo.completed === completed)
                // return this.todos.filter(function (todo) {
                //     return todo.completed === true ? true : false
                // })  // Array.filter() 参数是方法，相当于循环再判断，方法为过滤条件
            }
        },
        methods: { //在数据data()声明的层操作,不建议在下层操作
            addTodo(e) {    // event
                this.todos.unshift({
                    id: id++,
                    content: e.target.value.trim(),
                    completed: false
                })
                e.target.value = ''
            },
            deleteTodo(id) {
                // 点击一次删除按钮，每个item都会触发事件，所以根据编号的id找todos的下标，返回true false判断是否删除，因为todos长度变化不能直接根据传过来的id删除
                this.todos.splice(this.todos.findIndex(todo => todo.id === id), 1)
            },
            toggleFilter(state) {
                this.filter = state
            },
            clearAllCompleted(){
                this.todos = this.todos.filter(todo => !todo.completed)
            }
        }
    }
</script>

<style lang="stylus" scoped>
    .real-app
        width 600px
        margin 0 auto
        box-shadow 0 0 5px #666

    .add-input{
        position relative
        margin: 0;
        width 100%
        font-size 24px
        font-family inherit
        font-weight: inherit
        line-height: 1.4em
        border: 0
        outline none
        color inherit
        box-sizing: border-box
        font-smoothing: antialiased;
        padding: 16px 16px 16px 60px;
        border: none
        box-shadow: inset -2px 1px rgba(0,0,0,0.03)
    }



</style>