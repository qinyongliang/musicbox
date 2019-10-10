#include<stdio.h>
#import <Cocoa/Cocoa.h>
#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>
#import <IOKit/hidsystem/ev_keymap.h>

//Compile gcc -fobjc-arc -framework Cocoa -x objective-c -shared -o HotKey.lib hotkey.c
void (*play)(void);
void (*nextSong)(void);
void (*lastSong)(void);

void setContorllFunc(void (*playFunc)(void),void (*nextFunc)(void),void (*lastFunc)(void)){
    play = playFunc;
    nextSong = nextFunc;
    lastSong = lastFunc;
}

@interface HotKeyApp : NSApplication

@end

@implementation HotKeyApp
    - (void)sendEvent:(NSEvent*)anEvent{
        if([anEvent type] == NSEventTypeSystemDefined && [anEvent subtype] == 8){
            long data = [anEvent data1];
            int keyCode = ((data & 0xffff0000) >> 16);
            int keyFlags = (data & 0x0000ffff);
            int keyState = (((keyFlags & 0xff00) >> 8)) == 0xa;
            
            if(keyState){
                switch(keyCode){
                    case NX_KEYTYPE_PLAY:
                        play();
                        break;
                    
                    case NX_KEYTYPE_FAST:
                    case NX_KEYTYPE_NEXT:
                        nextSong();
                        break;
                    
                    case NX_KEYTYPE_REWIND:
                    case NX_KEYTYPE_PREVIOUS:
                        lastSong();
                        break;
                }
            }
            // return;
        }
	    // [super sendEvent:anEvent];
    }
@end
NSApplication* app;
void setup(){
    @autoreleasepool{
         app = [HotKeyApp sharedApplication];
        [app setActivationPolicy:NSApplicationActivationPolicyProhibited];
        [app activateIgnoringOtherApps:YES];
        [NSApp run];
    }
}

void stop(){
    @autoreleasepool{
        [NSApp terminate:app];
    }
}