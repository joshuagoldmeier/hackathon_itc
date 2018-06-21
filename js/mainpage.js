
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
        this.getItem();
     }

    getItem(){
       
        $.ajax({
            type:"GET",
            url:"/sports/ski",
            
            dataType:"json",
            success: function (response){
                // var item =[Name,Price,URL,Description,Image,Size];
                var counter = 0
                var row = $("<div>")
                row.addClass("row")
                console.log(Object.keys(response).length)
               for (var i = 0 ; i<Object.keys(response).length ; i++){

                   if (counter<2){
                        counter++;
                        var product =$("<div>")
                        product.addClass("col-6 product")
                        product.append("name: "+Object.values(response)[i].Name+"</br>")

                        product.append("price: "+Object.values(response)[i].Price+"</br")
            
                        product.append("url: "+Object.values(response)[i].URL+"</br>")

                        // product.append("Description: "+Object.values(response)[0].Description)
                        var image= $("<img>");

                        image.addClass("product-image")
                        image.attr("src",Object.values(response)[i].Image)
                        image.appendTo(product) 
                        // product.text("size: "+Object.values(response)[0].Size)

                        product.appendTo(row);   
                   }
                //    else{
                //         row.appendTo($(".items"));
                //        counter = 0;
                //        var row = $("<div>")
                //        row.addClass("row")
                //        var product =$("<div>")
                //        product.addClass("col-6 product")
                //        product.text("name: ")
                //        product.append(response[Object.keys(response)[i].Name]);
                //        product.text("name: ")
                //        product.append(response[Object.keys(response)[i].Price]);
                //        product.text("name: ")
                //        product.append(response[Object.keys(response)[i].URL]);
                //        product.text("name: ")
                //        product.append(response[Object.keys(response)[i].Description]);
                //        var image= $("<img>");
                //        image.addClass("product-image")
                //        image.attr("src",Object.values(response)[0].Image)
                //        image.appendTo(row); 
                //        product.append(response[Object.keys(response)[i].Size])
                //        product.appendTo(row);
                       
                //        counter++;
                       
                //    }
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
            <div className= "maincontainer">
                <h1>Hi <span>{this.state.name} </span><img id="headimg" src="../images/frobot.png"/> have found the best deals for you</h1>
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