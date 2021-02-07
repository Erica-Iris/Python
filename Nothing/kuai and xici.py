import ChangIp.GetAgent
import org.jsoup.Jsoup
import org.jsoup.nodes.Document

import scala.collection.mutable.ArrayBuffer
import scala.util.{Failure, Random, Success, Try}
import scala.collection.JavaConverters._

object IP_CollectTest {

  //抓取快代理前10页的ip
  def requestGetUrl(times:Int=20)(url:String,tag:String,arr_all:ArrayBuffer[String]): Unit ={
    //设置随机间隔时间
    var delay:Long=500
    delay = (1000+(new Random).nextInt(4000)).toLong

    //开始抓取
    //GetAgent.get_agent()方法--见上一篇，很简单，自己加一下就行
    Try(Jsoup.connect(url+tag).userAgent(GetAgent.get_agent()).get())match {
      case Failure(e) =>{
        if(times!=0){
          println(e.getMessage)
          //抓取失败重试
          Thread.sleep(delay)
          requestGetUrl(times-1)(url,tag,arr_all)
        }else throw e
      }
      case Success(doc) =>
        // 解析网页传入参数，doc和保存数据的数组
        val count = parseDoc(doc,arr_all)
        if (count==0){
          //抓取失败重试
          Thread.sleep(delay)
          if(times>=0){
            requestGetUrl(times-1)(url,tag,arr_all)
          }
          else {
            println(tag+"scrape data failed...,Please comfirm this word again")
          }
        }
    }
  }

  //网页解析
  def parseDoc(doc:Document,arr_all:ArrayBuffer[String]): Int ={
    // 用count判断是否有返回数据
    var count = 0
    val links = doc.select("tr")
    for(link<-links.asScala){
      // 爬取IP
      val ip = link.select("td").select("[data-title=IP]").text()
      // 爬取port
      val port = link.select("td").select("[data-title=PORT]").text()
      // 拼成字符串并保存
      if(!ip.isEmpty && !port.isEmpty){
        val res = ip+":"+port
        println(res)
        arr_all.append(res)
        // 有返回数据则count+1
        count+=1
      }
    }
    count
  }

  def use : ArrayBuffer[String] ={
    // 用一个array数组保存结果
    val arr_all = ArrayBuffer[String]()
    //遍历前10页
    for(i<-Range(1,11)){
      val url = "https://www.kuaidaili.com/free/inha/"
      // 传入三个参数（地址，页数，数组）
      requestGetUrl()(url,i.toString,arr_all)
    }
    //返回保存爬取数据的数组
    arr_all
  }

  def main(args: Array[String]): Unit = {
    use
  }
}