package
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	import flash.utils.getTimer;

	
	[SWF(width="1500", height="900", backgroundColor="#000000")]
	public class Test extends Sprite
	{
		
		private var progressiveLoader:ProgressiveLoader = new ProgressiveLoader();
		private var bitmap:Bitmap = new Bitmap();
		var textfied:TextField = new TextField();
		public function Test()
		{
			var fileName:String = root.loaderInfo.parameters.imgname;
			if(!fileName)
			{
				fileName = '1.jpg';
			}
			progressiveLoader.addEventListener("progressive_update", onUpdate);
			progressiveLoader.load(fileName);
			this.addChild(bitmap);
			
			
			textfied.defaultTextFormat = new TextFormat(null, 20);
			textfied.text = 'hello';
			textfied.autoSize = TextFieldAutoSize.LEFT;
			textfied.multiline = false;
			textfied.width = this.stage.stageWidth;
			textfied.backgroundColor = 0xFFFFFF;
			textfied.background = true;
			this.addChild(textfied);
		}
		
		private function changeColor(bitmapData:BitmapData, replace:Boolean):BitmapData
		{
			//color : ARBG 
			if(replace)
			{
				var colorToReplace:uint = 0xff808080;
				var newColor:uint = 0x000000;
				var maskToUse:uint = 0xffffffff;
				
				var rect:Rectangle = new Rectangle(0,0,bitmapData.width,bitmapData.height);
				var p:Point = new Point(0,0);
				//replace color
				bitmapData.threshold(bitmapData, rect, p, "==", colorToReplace, 
					newColor, maskToUse, true);
			}
			return bitmapData;
		}
		
		private function onUpdate(evt:Event):void
		{
			var bmd:BitmapData = progressiveLoader.bitmapdata;
			var color:uint = bmd.getPixel32(bmd.width - 1, bmd.height - 1);
			var replace:Boolean = true;
			trace(color == 0xff808080);
			trace(0xff808080, color);
			if(color != 0xff808080)
			{
				replace = false;
			}
			//现实最后的一个像素点的color
			textfied.textColor = color;
			//十进制转16进制
			textfied.text = color.toString(16) + '  ' + bmd.width + 'x' + bmd.height;
			
			var a:Number = getTimer();
			var bmd2:BitmapData = changeColor(bmd, replace);
			var b:Number = getTimer() - a;
			
			textfied.text = textfied.text + ' : ' + b + '->' + getTimer();
			bitmap.bitmapData = bmd2;
		}
	}
}