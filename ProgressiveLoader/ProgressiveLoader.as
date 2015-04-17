package
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.errors.IOError;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.net.URLRequest;
	import flash.net.URLStream;
	import flash.utils.ByteArray;

	public class ProgressiveLoader extends EventDispatcher
	{
		private var urlStream:URLStream;
		private var urlRequest:URLRequest;
		private var loader:Loader;
		private var byteArr:ByteArray;
		private var bmp:BitmapData = null;
		
		[Event(name = "progressive_update", type = "flash.events.Event")]
		public function ProgressiveLoader()
		{
			urlStream = new URLStream();
			urlRequest = new URLRequest();
			loader = new Loader();
			byteArr = new ByteArray();
			
			urlStream.addEventListener(ProgressEvent.PROGRESS, onStreamProgress);
			urlStream.addEventListener(Event.COMPLETE, onStreamComplete);
	urlStream.addEventListener(IOErrorEvent.IO_ERROR, onIOError);
			
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onComplete);
			loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, onComplete);
		}
		
		public function load(url:String):void
		{
			urlRequest.url = url;
			urlStream.load(urlRequest);
		}
		
		
		private function onStreamProgress(evt:ProgressEvent):void
		{
			if(!urlStream.bytesAvailable)
			{
				return;
			}
			urlStream.readBytes(byteArr, byteArr.length, urlStream.bytesAvailable);
			loader.unload();
			loader.loadBytes(byteArr);
		}
		
		private function onIOError(evt:IOErrorEvent):void
		{
			trace(evt.text);
		}
		
		public function get bitmapdata():BitmapData
		{
			return bmp;
		}
		
		private function onStreamComplete(evt:Event):void
		{
			onStreamProgress(null);
		}
		
		private function onComplete(evt:Event):void
		{
			if(loader.content)
			{
				bmp = Bitmap(loader.content).bitmapData;
				dispatchEvent(new Event("progressive_update", false, false));
			}
		}
	}
}