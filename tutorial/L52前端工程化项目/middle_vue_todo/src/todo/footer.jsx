// vue, jsx 最终转成render ,createElement
export default {
    data(){
        return {
            author: 'Jokcy'
        }
    },
    render(){
        return (
            <div id="footer" style="position: absolute; right:0px;bottom:0px;">
                <span>Written by {this.author}</span>
            </div>

        )
    }
}