定义属性
public static var goodsInfo:String = "testinfo";


OnBeforeRequest 方法中添加
goodsInfo = oSession.GetRequestBodyAsString()


OnBeforeResponse 方法中添加

if (oSession.fullUrl.Contains("m.poizon.com/product/detail"))
    //if (oSession.fullUrl.Contains("baidu"))
{
    var _xhr = new ActiveXObject('Microsoft.XMLHTTP');
    var url = 'http://sport.baidu.com/Spider/ducloseinfo';
    //发送的数据参数

    var _data = encodeURIComponent(oSession.GetResponseBodyAsString());
        
    //不需要返回值所以写啦个空回调
    _xhr.onreadystatechange = function() {}
    _xhr.open('POST', url, true);
    _xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    _xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    _xhr.send(_data);
}
//毒 评论
if (oSession.fullUrl.Contains("m.poizon.com/product/lastSoldList"))
    //if (oSession.fullUrl.Contains("baidu"))
{
    var _xhr = new ActiveXObject('Microsoft.XMLHTTP');
    var url = 'http://sport.baidu.com/Spider/dubuyhistory?'+oSession.url.Split("?")[1];
    //发送的数据参数
       
    
    var _data = encodeURIComponent(oSession.GetResponseBodyAsString());
    //不需要返回值所以写啦个空回调
    _xhr.onreadystatechange = function() {}
    _xhr.open('POST', url, true);
    _xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    _xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    _xhr.send(_data);
}


if (oSession.fullUrl.Contains("api.oneniceapp.com/Product/detail"))
    //if (oSession.fullUrl.Contains("baidu"))
{
    var _xhr = new ActiveXObject('Microsoft.XMLHTTP');
    var url = 'http://sport.baidu.com/Spider/nicecloseinfo';
    //发送的数据参数

    var _data = encodeURIComponent(oSession.GetResponseBodyAsString());
    //不需要返回值所以写啦个空回调
    _xhr.onreadystatechange = function() {}
    _xhr.open('POST', url, true);
    _xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    _xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    _xhr.send(_data);
}
//nice评论

if (oSession.fullUrl.Contains("api.oneniceapp.com/Product/tradeRecord"))
    //if (oSession.fullUrl.Contains("baidu"))
{
    var _xhr = new ActiveXObject('Microsoft.XMLHTTP');
    var url = 'http://sport.baidu.com/Spider/nicehistory?goodsinfo='+goodsInfo;
    //发送的数据参数

    var _data = encodeURIComponent(oSession.GetResponseBodyAsString());
    //不需要返回值所以写啦个空回调
    _xhr.onreadystatechange = function() {}
    _xhr.open('POST', url, true);
    _xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    _xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    _xhr.send(_data);
}