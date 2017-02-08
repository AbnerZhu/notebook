# Java Concurrent

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;

public class ConcurrentTest {
	private static int thread_num = 200;
	private static int client_num = 500;

	public static void main(String[] args) {
		ExecutorService exec = Executors.newCachedThreadPool();

		final Semaphore semp = new Semaphore(thread_num);

		for (int index = 0; index < client_num; index++) {

			final int NO = index;

			Runnable run = new Runnable() {
				public void run() {
					try {
						semp.acquire();
						System.out.println("Thread:" + NO);
						//业务逻辑
						semp.release();
					} catch (Exception e) {
						e.printStackTrace();
					}
				}
			};
			exec.execute(run);
		}
		exec.shutdown();
	}
}
```

```java
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import org.apache.log4j.Logger;

// java并发发送请求的示例
public class ConcurrentRuleSyncUtil {

	private static final int MAX_THREAD = 10;  //最多启动的线程数

	private static final ExecutorService exec = Executors.newFixedThreadPool(MAX_THREAD);
	
	private static final Logger logger = Logger.getLogger(ConcurrentRuleSyncUtil.class);

	/**
	 * 并发来主动通知所有应用来更新规则 最多启动
	 * 
	 * @param strUrl
	 *            需要通知的应用ip列表
	 * @return
	 */
	public static List<String> activeAppList(List<String> strUrl, String queryString) {
		if (strUrl == null || strUrl.size() == 0) {
			return null;
		}
		List<Callable<List<String>>> runThreads = GeneralThreadInfo(strUrl,queryString);
		List<String> resList = new ArrayList<String>();
		try {
			List<Future<List<String>>> fetures = exec.invokeAll(runThreads);
			for(Future<List<String>> feture: fetures){
				List<String> tmp = null;
				try {
					tmp = feture.get();
				} catch (ExecutionException e) {
					logger.error("ConcurrentRuleSyncUtil thread activeAppList get error:" + e.getMessage(), e);
				}
				if(tmp != null){
					resList.addAll(tmp);
				}
			}
		} catch (InterruptedException e) {
			logger.error("ConcurrentRuleSyncUtil activeAppList get error:" + e.getMessage(), e);
		}
		return resList;
	}

	public static List<Callable<List<String>>> GeneralThreadInfo(List<String> strUrl, String queryString) {
		List<Callable<List<String>>> runThreads = new ArrayList<Callable<List<String>>>();
		int size = strUrl.size() / MAX_THREAD + 1;
		int i = 0;
		int len = strUrl.size();
		for(; i + size <= len; i += size){
			runThreads.add(new ActiveSyncThread(strUrl.subList(i, i + size), queryString));
		}
		if(i < len){
			runThreads.add(new ActiveSyncThread(strUrl.subList(i,len), queryString));	
		}
		return runThreads;
	}
	
	static class ActiveSyncThread  implements Callable<List<String>>{

		private List<String> hostlistUrl;  //分配到当前线程的host列表
		private String queryString;  //参数串
		
		public ActiveSyncThread(List<String> strUrl, String queryString){
			this.hostlistUrl = strUrl;
			this.queryString = queryString;
		}		

		@Override
		public List<String> call() throws Exception {
			return getResponseText(hostlistUrl+queryString);
		}
		
	}
/**
	 * 根据绑定去查询绑定地址的url html,HttpUrlConnection调用方式
	 * 
	 * @param url
	 *            查询的url
	 * @throws IOException
	 */
	public static String getResponseText(String queryUrl) {
		return getResponseText(queryUrl, null, null);
	}
	/**
	 * 根据绑定去查询绑定地址的url html,HttpUrlConnection调用方式
	 * 
	 * @param url
	 *            查询的url
	 * @param host
	 *            需要绑定的host
	 * @param ip
	 *            对应host绑定的ip
	 * @throws IOException
	 */
	public static String getResponseText(String queryUrl,String host,String ip) {
		InputStream is = null;
		BufferedReader br = null;
		StringBuffer res = new StringBuffer();
		try {
			HttpURLConnection httpUrlConn = null;
			URL url = new URL(queryUrl);
			if(ip!=null){
			    String str[] = ip.split("\\.");
			    byte[] b =new byte[str.length];
			    for(int i=0,len=str.length;i<len;i++){
			        b[i] = (byte)(Integer.parseInt(str[i],10));
			    }
	            Proxy proxy = new Proxy(Proxy.Type.HTTP,
	            new InetSocketAddress(InetAddress.getByAddress(b), 80));
	            httpUrlConn = (HttpURLConnection) url
                .openConnection(proxy);
			}else{
	            httpUrlConn = (HttpURLConnection) url
	                    .openConnection();
			}
			httpUrlConn.setRequestMethod("GET");
			httpUrlConn.setDoOutput(true);
			httpUrlConn.setConnectTimeout(DEFAULT_TIMEOUT);
			httpUrlConn.setReadTimeout(DEFAULT_TIMEOUT);
			httpUrlConn.setDefaultUseCaches(false);
			httpUrlConn.setUseCaches(false);

			is = httpUrlConn.getInputStream();

			int responseCode = httpUrlConn.getResponseCode();
			// 如果返回的结果是400以上，那么就说明出问题了
			if (responseCode > 400) {
				logger.error("getResponseText for queryurl:" + queryUrl + " got responseCode :" + responseCode);
				return "getResponseText for queryurl:" + queryUrl + " got responseCode :" + responseCode;
			}
			// 需要自动识别页面的编码，通过从context-type中解析得到，默认为UTF-8
			String encoding = "UTF-8";
			String contextType = httpUrlConn.getContentType();
			if (StringUtilsExt.isNotBlank(contextType)) {
				int pos = contextType.lastIndexOf("=");
				if (pos > -1) {
					encoding = contextType.substring(pos + 1);
				}
			}
			// System.out.println(encoding);

			br = new BufferedReader(new InputStreamReader(is, encoding));

			String data = null;
			while ((data = br.readLine()) != null) {
				res.append(data + "\n");
			}
			return res.toString();

		} catch (IOException e) {
            logger.error(e.getMessage(), e);
            return "failed: " + e.getMessage();
		} catch (Exception e) {
		    logger.error(e.getMessage(), e);
		    return "failed: " + e.getMessage();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
		            logger.error(e.getMessage(), e);
		            res.append(e.getMessage());
				}
			}
		}
	}
}
```

