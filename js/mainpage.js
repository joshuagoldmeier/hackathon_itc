
class MainPage extends React.Component{
    constructor(props){
        super(props); 
        this.getItem =this.getItem.bind(this)
        this.state={
            name: document.cookie.substring(5)
        }
    }

    componentDidMount() {
        this.getItem()
     }

    getItem(){
        console.log(document.cookie.substring(5))
        $.ajax({
            type:"GET",
            url:"/sports/ski",
            
            dataType:"json",
            success: function (response){
                var counter = 0
                var row = $("<div>")
                row.addClass("row")
               for (var i = 0 ; i<response.length ; i++){
                   if (counter<2){
                        counter++;
                        var product =$("<div>")
                        product.addClass("col-6 product")
                        product.append(response[i])
                        product.appendTo(row);   
                   }
                   else{
                        row.appendTo($(".items"));
                       counter = 0;
                       var row = $("<div>")
                       row.addClass("row")
                       var product =$("<div>")
                       product.addClass("col-6 product")
                       product.append(response[i])
                       product.appendTo(row);
                       
                       counter++;
                       
                   }
               }
               row.appendTo($(".items")); 
            },
            
            error: function(msg){
                console.log("error");
            },
    
        });
    }
    render(){
        return(
            <div>
                <h1>Hi <span>{this.state.name}</span> We found the best deals for you</h1>
                <div className="displayBy">
                    <div className="container">
                        <div className="row">
                            <button className="col-6">Display By Rates</button>
                            <button className="col-6">Display By Prices</button>
                        </div>
                    </div>
                </div>
                <div className="items container"></div>
            </div>
        )
    }
}

ReactDOM.render(

    <MainPage/>,
    document.getElementById("root")
);