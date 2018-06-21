
class MainPage extends React.Component{
    constructor(props){
        super(props); 
        this.getItem =this.getItem.bind(this)
        var cookieSplitted = document.cookie.split(";");
        this.state={
            name: cookieSplitted[1].substring(6),
            sport : cookieSplitted[0].substring(7)
        }
    }

    componentDidMount() {
        // window.addEventListener('load', this.getItem);
        this.getItem();
     }

    getItem(){
       
        $.ajax({
            type:"GET",
            url:"/sports/ski",
            
            dataType:"json",
            success: function (response){
                console.log(response)
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
                <h1>Hi <span>{this.state.name}</span> we found the best deals for you</h1>
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