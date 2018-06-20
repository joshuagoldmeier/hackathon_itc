
class MainPage extends React.Component{
    constructor(props){
        super(props); 
        this.getItem =this.getItem.bind(this)
    }
    getItem(){
        $.ajax({
            type:"GET",
            url:"/sports/ski",
            
            dataType:"json",
            success: function (response){
               console.log(response)
            },
            
            error: function(msg){
                console.log("error");
            },
    
        });
    }
    render(){
        return(
            <div class="item" onLoad={this.getItem}>bb</div>
        )
    }
}

ReactDOM.render(

    <MainPage/>,
    document.getElementById("root")
);