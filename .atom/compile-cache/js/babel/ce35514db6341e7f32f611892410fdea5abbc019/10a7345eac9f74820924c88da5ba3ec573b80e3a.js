Object.defineProperty(exports, '__esModule', {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

var _atom = require('atom');

'use babel';

var AtomClockView = (function () {
  function AtomClockView(statusBar) {
    _classCallCheck(this, AtomClockView);

    this.statusBar = statusBar;
    this.subscriptions = new _atom.CompositeDisposable();
  }

  _createClass(AtomClockView, [{
    key: 'start',
    value: function start() {
      this.drawElement();
      this.initialize();
    }
  }, {
    key: 'initialize',
    value: function initialize() {
      var _this = this;

      this.setConfigValues();
      this.setTooltip(this.showTooltip);
      this.setIcon(this.showIcon);
      this.toClipboard(this.rightClickToClipboard);
      this.setUTCClass(this.showUTC);
      this.startTicker();

      this.subscriptions.add(atom.commands.add('atom-workspace', {
        'atom-clock:toggle': function atomClockToggle() {
          return _this.toggle();
        },
        'atom-clock:utc-mode': function atomClockUtcMode() {
          return atom.config.set('atom-clock.showUTC', !_this.showUTC);
        }
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.dateFormat', function () {
        _this.refreshTicker();
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.showTooltip', function () {
        _this.setConfigValues();
        _this.setTooltip(_this.showTooltip);
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.tooltipDateFormat', function () {
        _this.refreshTicker();
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.locale', function () {
        _this.refreshTicker();
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.showUTC', function () {
        _this.refreshTicker();
        _this.setUTCClass(_this.showUTC);
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.refreshInterval', function () {
        _this.refreshTicker();
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.showClockIcon', function () {
        _this.setConfigValues();
        _this.setIcon(_this.showIcon);
      }));

      if (this.showOnlyInFullscreen) this.element.classList.add('fullscreen-hide');else this.element.classList.remove('fullscreen-hide');

      this.subscriptions.add(atom.config.onDidChange('atom-clock.showOnlyInFullscreen', function () {
        _this.showOnlyInFullscreen = !_this.showOnlyInFullscreen;
        _this.element.classList.toggle('fullscreen-hide');
      }));

      this.subscriptions.add(atom.config.onDidChange('atom-clock.rightClickToClipboard', function () {
        _this.rightClickToClipboard = !_this.rightClickToClipboard;
        _this.toClipboard(_this.rightClickToClipboard);
      }));
    }
  }, {
    key: 'drawElement',
    value: function drawElement() {
      this.element = document.createElement('div');
      this.element.classList.add('atom-clock', 'inline-block');

      this.iconElement = document.createElement('span');
      this.iconElement.classList.add('atom-clock-icon');

      this.timeElement = document.createElement('span');
      this.timeElement.classList.add('atom-clock-time');

      this.element.appendChild(this.iconElement);
      this.element.appendChild(this.timeElement);

      this.statusBar.addRightTile({
        item: this.element,
        priority: -500
      });
    }
  }, {
    key: 'setConfigValues',
    value: function setConfigValues() {
      this.dateFormat = atom.config.get('atom-clock.dateFormat');
      this.showTooltip = atom.config.get('atom-clock.showTooltip');
      this.tooltipDateFormat = atom.config.get('atom-clock.tooltipDateFormat');
      this.locale = atom.config.get('atom-clock.locale');
      this.showUTC = atom.config.get('atom-clock.showUTC');
      this.refreshInterval = atom.config.get('atom-clock.refreshInterval') * 1000;
      this.showIcon = atom.config.get('atom-clock.showClockIcon');
      this.showOnlyInFullscreen = atom.config.get('atom-clock.showOnlyInFullscreen');
      this.rightClickToClipboard = atom.config.get('atom-clock.rightClickToClipboard');
    }
  }, {
    key: 'startTicker',
    value: function startTicker() {
      var _this2 = this;

      this.setDate();
      var nextTick = this.refreshInterval - Date.now() % this.refreshInterval;
      this.tick = setTimeout(function () {
        _this2.startTicker();
      }, nextTick);
    }
  }, {
    key: 'clearTicker',
    value: function clearTicker() {
      if (this.tick) clearTimeout(this.tick);
    }
  }, {
    key: 'refreshTicker',
    value: function refreshTicker() {
      this.setConfigValues();
      this.clearTicker();
      this.startTicker();
    }
  }, {
    key: 'setDate',
    value: function setDate() {
      this.date = this.getDate(this.locale, this.dateFormat);
      this.timeElement.textContent = this.date;
    }
  }, {
    key: 'getDate',
    value: function getDate(locale, format) {
      if (!this.Moment) this.Moment = require('moment');

      var moment = this.Moment().locale(locale);

      if (this.showUTC) moment.utc();

      return moment.format(format);
    }
  }, {
    key: 'setIcon',
    value: function setIcon(toSet) {
      if (toSet) this.iconElement.classList.add('icon', 'icon-clock');else this.iconElement.classList.remove('icon', 'icon-clock');
    }
  }, {
    key: 'setTooltip',
    value: function setTooltip(toSet) {
      var _this3 = this;

      if (this.tooltip === undefined) this.tooltip = atom.tooltips.add(this.element, {
        title: function title() {
          return _this3.getDate(_this3.locale, _this3.tooltipDateFormat);
        },
        'class': 'atom-clock-tooltip'
      });

      if (toSet) atom.tooltips.findTooltips(this.element)[0].enable();else atom.tooltips.findTooltips(this.element)[0].disable();
    }
  }, {
    key: 'toClipboard',
    value: function toClipboard(toSet) {
      var _this4 = this;

      if (toSet) {
        this.element.oncontextmenu = function () {
          atom.clipboard.write(_this4.getDate(_this4.locale, _this4.tooltipDateFormat));
          atom.notifications.addSuccess('Current time copied to clipboard.', {
            dismissable: true,
            icon: 'clock'
          });
        };
      } else {
        this.element.oncontextmenu = null;
      }
    }
  }, {
    key: 'setUTCClass',
    value: function setUTCClass(toSet) {
      if (toSet) {
        this.element.classList.add('atom-clock-utc');
        atom.tooltips.findTooltips(this.element)[0].getTooltipElement().classList.add('atom-clock-utc');
      } else {
        this.element.classList.remove('atom-clock-utc');
        atom.tooltips.findTooltips(this.element)[0].getTooltipElement().classList.remove('atom-clock-utc');
      }
    }
  }, {
    key: 'toggle',
    value: function toggle() {
      var style = this.element.style.display;
      this.element.style.display = style === 'none' ? '' : 'none';
    }
  }, {
    key: 'destroy',
    value: function destroy() {
      this.clearTicker();
      this.subscriptions.dispose();
      this.tooltip.dispose();
      this.element.remove();
    }
  }]);

  return AtomClockView;
})();

exports['default'] = AtomClockView;
module.exports = exports['default'];
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9Vc2Vycy9qYXZpZXIvLmF0b20vcGFja2FnZXMvYXRvbS1jbG9jay9saWIvYXRvbS1jbG9jay12aWV3LmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7O29CQUVvQyxNQUFNOztBQUYxQyxXQUFXLENBQUM7O0lBSVMsYUFBYTtBQUVyQixXQUZRLGFBQWEsQ0FFcEIsU0FBUyxFQUFFOzBCQUZKLGFBQWE7O0FBRzlCLFFBQUksQ0FBQyxTQUFTLEdBQUcsU0FBUyxDQUFBO0FBQzFCLFFBQUksQ0FBQyxhQUFhLEdBQUcsK0JBQXlCLENBQUE7R0FDL0M7O2VBTGtCLGFBQWE7O1dBTzNCLGlCQUFHO0FBQ04sVUFBSSxDQUFDLFdBQVcsRUFBRSxDQUFBO0FBQ2xCLFVBQUksQ0FBQyxVQUFVLEVBQUUsQ0FBQTtLQUNsQjs7O1dBRVMsc0JBQUc7OztBQUNYLFVBQUksQ0FBQyxlQUFlLEVBQUUsQ0FBQTtBQUN0QixVQUFJLENBQUMsVUFBVSxDQUFDLElBQUksQ0FBQyxXQUFXLENBQUMsQ0FBQTtBQUNqQyxVQUFJLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxRQUFRLENBQUMsQ0FBQTtBQUMzQixVQUFJLENBQUMsV0FBVyxDQUFDLElBQUksQ0FBQyxxQkFBcUIsQ0FBQyxDQUFBO0FBQzVDLFVBQUksQ0FBQyxXQUFXLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxDQUFBO0FBQzlCLFVBQUksQ0FBQyxXQUFXLEVBQUUsQ0FBQTs7QUFFbEIsVUFBSSxDQUFDLGFBQWEsQ0FBQyxHQUFHLENBQUMsSUFBSSxDQUFDLFFBQVEsQ0FBQyxHQUFHLENBQUMsZ0JBQWdCLEVBQUU7QUFDekQsMkJBQW1CLEVBQUU7aUJBQU0sTUFBSyxNQUFNLEVBQUU7U0FBQTtBQUN4Qyw2QkFBcUIsRUFBRTtpQkFBTSxJQUFJLENBQUMsTUFBTSxDQUFDLEdBQUcsQ0FBQyxvQkFBb0IsRUFBRSxDQUFDLE1BQUssT0FBTyxDQUFDO1NBQUE7T0FDbEYsQ0FBQyxDQUFDLENBQUE7O0FBRUgs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QTtLQUM1RDs7O1dBRU0sbUJBQUc7QUFDUixVQUFJLENBQUMsV0FBVyxFQUFFLENBQUE7QUFDbEIsVUFBSSxDQUFDLGFBQWEsQ0FBQyxPQUFPLEVBQUUsQ0FBQTtBQUM1QixVQUFJLENBQUMsT0FBTyxDQUFDLE9BQU8sRUFBRSxDQUFBO0FBQ3RCLFVBQUksQ0FBQyxPQUFPLENBQUMsTUFBTSxFQUFFLENBQUE7S0FDdEI7OztTQWpNa0IsYUFBYTs7O3FCQUFiLGFBQWEiLCJmaWxlIjoiL1VzZXJzL2phdmllci8uYXRvbS9wYWNrYWdlcy9hdG9tLWNsb2NrL2xpYi9hdG9tLWNsb2NrLXZpZXcuanMiLCJzb3VyY2VzQ29udGVudCI6WyIndXNlIGJhYmVsJztcblxuaW1wb3J0IHsgQ29tcG9zaXRlRGlzcG9zYWJsZSB9IGZyb20gJ2F0b20nXG5cbmV4cG9ydCBkZWZhdWx0IGNsYXNzIEF0b21DbG9ja1ZpZXcge1xuXG4gIGNvbnN0cnVjdG9yKHN0YXR1c0Jhcikge1xuICAgIHRoaXMuc3RhdHVzQmFyID0gc3RhdHVzQmFyXG4gICAgdGhpcy5zdWJzY3JpcHRpb25zID0gbmV3IENvbXBvc2l0ZURpc3Bvc2FibGUoKVxuICB9XG5cbiAgc3RhcnQoKSB7XG4gICAgdGhpcy5kcmF3RWxlbWVudCgpXG4gICAgdGhpcy5pbml0aWFsaXplKClcbiAgfVxuXG4gIGluaXRpYWxpemUoKSB7XG4gICAgdGhpcy5zZXRDb25maWdWYWx1ZXMoKVxuICAgIHRoaXMuc2V0VG9vbHRpcCh0aGlzLnNob3dUb29sdGlwKVxuICAgIHRoaXMuc2V0SWNvbih0aGlzLnNob3dJY29uKVxuICAgIHRoaXMudG9DbGlwYm9hcmQodGhpcy5yaWdodENsaWNrVG9DbGlwYm9hcmQpXG4gICAgdGhpcy5zZXRVVENDbGFzcyh0aGlzLnNob3dVVEMpXG4gICAgdGhpcy5zdGFydFRpY2tlcigpXG5cbiAgICB0aGlzLnN1YnNjcmlwdGlvbnMuYWRkKGF0b20uY29tbWFuZHMuYWRkKCdhdG9tLXdvcmtzcGFjZScsIHtcbiAgICAgICdhdG9tLWNsb2NrOnRvZ2dsZSc6ICgpID0+IHRoaXMudG9nZ2xlKCksXG4gICAgICAnYXRvbS1jbG9jazp1dGMtbW9kZSc6ICgpID0+IGF0b20uY29uZmlnLnNldCgnYXRvbS1jbG9jay5zaG93VVRDJywgIXRoaXMuc2hvd1VUQylcbiAgICB9KSlcblxuICAgIHRoaXMuc3Vic2NyaXB0aW9ucy5hZGQoYXRvbS5jb25maWcub25EaWRDaGFuZ2UoJ2F0b20tY2xvY2suZGF0ZUZvcm1hdCcsICgpID0+IHtcbiAgICAgIHRoaXMucmVmcmVzaFRpY2tlcigpXG4gICAgfSkpXG5cbiAgICB0aGlzLnN1YnNjcmlwdGlvbnMuYWRkKGF0b20uY29uZmlnLm9uRGlkQ2hhbmdlKCdhdG9tLWNsb2NrLnNob3dUb29sdGlwJywgKCkgPT4ge1xuICAgICAgdGhpcy5zZXRDb25maWdWYWx1ZXMoKVxuICAgICAgdGhpcy5zZXRUb29sdGlwKHRoaXMuc2hvd1Rvb2x0aXApXG4gICAgfSkpXG5cbiAgICB0aGlzLnN1YnNjcmlwdGlvbnMuYWRkKGF0b20uY29uZmlnLm9uRGlkQ2hhbmdlKCdhdG9tLWNsb2NrLnRvb2x0aXBEYXRlRm9ybWF0JywgKCkgPT4ge1xuICAgICAgdGhpcy5yZWZyZXNoVGlja2VyKClcbiAgICB9KSlcblxuICAgIHRoaXMuc3Vic2NyaXB0aW9ucy5hZGQoYXRvbS5jb25maWcub25EaWRDaGFuZ2UoJ2F0b20tY2xvY2subG9jYWxlJywgKCkgPT4ge1xuICAgICAgdGhpcy5yZWZyZXNoVGlja2VyKClcbiAgICB9KSlcblxuICAgIHRoaXMuc3Vic2NyaXB0aW9ucy5hZGQoYXRvbS5jb25maWcub25EaWRDaGFuZ2UoJ2F0b20tY2xvY2suc2hvd1VUQycsICgpID0+IHtcbiAgICAgIHRoaXMucmVmcmVzaFRpY2tlcigpXG4gICAgICB0aGlzLnNldFVUQ0NsYXNzKHRoaXMuc2hvd1VUQylcbiAgICB9KSlcblxuICAgIHRoaXMuc3Vic2NyaXB0aW9ucy5hZGQoYXRvbS5jb25maWcub25EaWRDaGFuZ2UoJ2F0b20tY2xvY2sucmVmcmVzaEludGVydmFsJywgKCkgPT4ge1xuICAgICAgdGhpcy5yZWZyZXNoVGlja2VyKClcbiAgICB9KSlcblxuICAgIHRoaXMuc3Vic2NyaXB0aW9ucy5hZGQoYXRvbS5jb25maWcub25EaWRDaGFuZ2UoJ2F0b20tY2xvY2suc2hvd0Nsb2NrSWNvbicsICgpID0+IHtcbiAgICAgIHRoaXMuc2V0Q29uZmlnVmFsdWVzKClcbiAgICAgIHRoaXMuc2V0SWNvbih0aGlzLnNob3dJY29uKVxuICAgIH0pKVxuXG4gICAgaWYgKHRoaXMuc2hvd09ubHlJbkZ1bGxzY3JlZW4pXG4gICAgICB0aGlzLmVsZW1lbnQuY2xhc3NMaXN0LmFkZCgnZnVsbHNjcmVlbi1oaWRlJylcbiAgICBlbHNlXG4gICAgICB0aGlzLmVsZW1lbnQuY2xhc3NMaXN0LnJlbW92ZSgnZnVsbHNjcmVlbi1oaWRlJylcblxuICAgIHRoaXMuc3Vic2NyaXB0aW9ucy5hZGQoYXRvbS5jb25maWcub25EaWRDaGFuZ2UoJ2F0b20tY2xvY2suc2hvd09ubHlJbkZ1bGxzY3JlZW4nLCAoKSA9PiB7XG4gICAgICB0aGlzLnNob3dPbmx5SW5GdWxsc2NyZWVuID0gIXRoaXMuc2hvd09ubHlJbkZ1bGxzY3JlZW5cbiAgICAgIHRoaXMuZWxlbWVudC5jbGFzc0xpc3QudG9nZ2xlKCdmdWxsc2NyZWVuLWhpZGUnKVxuICAgIH0pKVxuXG4gICAgdGhpcy5zdWJzY3JpcHRpb25zLmFkZChhdG9tLmNvbmZpZy5vbkRpZENoYW5nZSgnYXRvbS1jbG9jay5yaWdodENsaWNrVG9DbGlwYm9hcmQnLCAoKSA9PiB7XG4gICAgICB0aGlzLnJpZ2h0Q2xpY2tUb0NsaXBib2FyZCA9ICF0aGlzLnJpZ2h0Q2xpY2tUb0NsaXBib2FyZFxuICAgICAgdGhpcy50b0NsaXBib2FyZCh0aGlzLnJpZ2h0Q2xpY2tUb0NsaXBib2FyZClcbiAgICB9KSlcblxuICB9XG5cbiAgZHJhd0VsZW1lbnQoKSB7XG4gICAgdGhpcy5lbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2JylcbiAgICB0aGlzLmVsZW1lbnQuY2xhc3NMaXN0LmFkZCgnYXRvbS1jbG9jaycsICdpbmxpbmUtYmxvY2snKVxuXG4gICAgdGhpcy5pY29uRWxlbWVudCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NwYW4nKVxuICAgIHRoaXMuaWNvbkVsZW1lbnQuY2xhc3NMaXN0LmFkZCgnYXRvbS1jbG9jay1pY29uJylcblxuICAgIHRoaXMudGltZUVsZW1lbnQgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzcGFuJylcbiAgICB0aGlzLnRpbWVFbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2F0b20tY2xvY2stdGltZScpXG5cbiAgICB0aGlzLmVsZW1lbnQuYXBwZW5kQ2hpbGQodGhpcy5pY29uRWxlbWVudClcbiAgICB0aGlzLmVsZW1lbnQuYXBwZW5kQ2hpbGQodGhpcy50aW1lRWxlbWVudClcblxuICAgIHRoaXMuc3RhdHVzQmFyLmFkZFJpZ2h0VGlsZSh7XG4gICAgICBpdGVtOiB0aGlzLmVsZW1lbnQsXG4gICAgICBwcmlvcml0eTogLTUwMFxuICAgIH0pXG4gIH1cblxuICBzZXRDb25maWdWYWx1ZXMoKSB7XG4gICAgdGhpcy5kYXRlRm9ybWF0ID0gYXRvbS5jb25maWcuZ2V0KCdhdG9tLWNsb2NrLmRhdGVGb3JtYXQnKVxuICAgIHRoaXMuc2hvd1Rvb2x0aXAgPSBhdG9tLmNvbmZpZy5nZXQoJ2F0b20tY2xvY2suc2hvd1Rvb2x0aXAnKVxuICAgIHRoaXMudG9vbHRpcERhdGVGb3JtYXQgPSBhdG9tLmNvbmZpZy5nZXQoJ2F0b20tY2xvY2sudG9vbHRpcERhdGVGb3JtYXQnKVxuICAgIHRoaXMubG9jYWxlID0gYXRvbS5jb25maWcuZ2V0KCdhdG9tLWNsb2NrLmxvY2FsZScpXG4gICAgdGhpcy5zaG93VVRDID0gYXRvbS5jb25maWcuZ2V0KCdhdG9tLWNsb2NrLnNob3dVVEMnKVxuICAgIHRoaXMucmVmcmVzaEludGVydmFsID0gYXRvbS5jb25maWcuZ2V0KCdhdG9tLWNsb2NrLnJlZnJlc2hJbnRlcnZhbCcpICogMTAwMFxuICAgIHRoaXMuc2hvd0ljb24gPSBhdG9tLmNvbmZpZy5nZXQoJ2F0b20tY2xvY2suc2hvd0Nsb2NrSWNvbicpXG4gICAgdGhpcy5zaG93T25seUluRnVsbHNjcmVlbiA9IGF0b20uY29uZmlnLmdldCgnYXRvbS1jbG9jay5zaG93T25seUluRnVsbHNjcmVlbicpXG4gICAgdGhpcy5yaWdodENsaWNrVG9DbGlwYm9hcmQgPSBhdG9tLmNvbmZpZy5nZXQoJ2F0b20tY2xvY2sucmlnaHRDbGlja1RvQ2xpcGJvYXJkJylcbiAgfVxuXG4gIHN0YXJ0VGlja2VyKCkge1xuICAgIHRoaXMuc2V0RGF0ZSgpXG4gICAgdmFyIG5leHRUaWNrID0gdGhpcy5yZWZyZXNoSW50ZXJ2YWwgLSAoRGF0ZS5ub3coKSAlIHRoaXMucmVmcmVzaEludGVydmFsKVxuICAgIHRoaXMudGljayA9IHNldFRpbWVvdXQgKCgpID0+ICB7IHRoaXMuc3RhcnRUaWNrZXIoKSB9LCBuZXh0VGljaylcbiAgfVxuXG4gIGNsZWFyVGlja2VyKCkge1xuICAgIGlmICh0aGlzLnRpY2spXG4gICAgICBjbGVhclRpbWVvdXQodGhpcy50aWNrKVxuICB9XG5cbiAgcmVmcmVzaFRpY2tlcigpIHtcbiAgICB0aGlzLnNldENvbmZpZ1ZhbHVlcygpXG4gICAgdGhpcy5jbGVhclRpY2tlcigpXG4gICAgdGhpcy5zdGFydFRpY2tlcigpXG4gIH1cblxuICBzZXREYXRlKCkge1xuICAgIHRoaXMuZGF0ZSA9IHRoaXMuZ2V0RGF0ZSh0aGlzLmxvY2FsZSwgdGhpcy5kYXRlRm9ybWF0KVxuICAgIHRoaXMudGltZUVsZW1lbnQudGV4dENvbnRlbnQgPSB0aGlzLmRhdGVcbiAgfVxuXG4gIGdldERhdGUobG9jYWxlLCBmb3JtYXQpIHtcbiAgICBpZiAoIXRoaXMuTW9tZW50KVxuICAgICAgdGhpcy5Nb21lbnQgPSByZXF1aXJlKCdtb21lbnQnKVxuXG4gICAgdmFyIG1vbWVudCA9IHRoaXMuTW9tZW50KCkubG9jYWxlKGxvY2FsZSlcblxuICAgIGlmICh0aGlzLnNob3dVVEMpXG4gICAgICBtb21lbnQudXRjKClcblxuICAgIHJldHVybiBtb21lbnQuZm9ybWF0KGZvcm1hdClcbiAgfVxuXG4gIHNldEljb24odG9TZXQpIHtcbiAgICBpZiAodG9TZXQpXG4gICAgICB0aGlzLmljb25FbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2ljb24nLCAnaWNvbi1jbG9jaycpXG4gICAgZWxzZVxuICAgICAgdGhpcy5pY29uRWxlbWVudC5jbGFzc0xpc3QucmVtb3ZlKCdpY29uJywgJ2ljb24tY2xvY2snKVxuICB9XG5cbiAgc2V0VG9vbHRpcCh0b1NldCkge1xuICAgIGlmICh0aGlzLnRvb2x0aXAgPT09IHVuZGVmaW5lZClcbiAgICAgIHRoaXMudG9vbHRpcCA9IGF0b20udG9vbHRpcHMuYWRkKHRoaXMuZWxlbWVudCwge1xuICAgICAgICB0aXRsZTogKCkgPT4gdGhpcy5nZXREYXRlKHRoaXMubG9jYWxlLCB0aGlzLnRvb2x0aXBEYXRlRm9ybWF0KSxcbiAgICAgICAgY2xhc3M6ICdhdG9tLWNsb2NrLXRvb2x0aXAnXG4gICAgICB9KVxuXG4gICAgaWYgKHRvU2V0KVxuICAgICAgYXRvbS50b29sdGlwcy5maW5kVG9vbHRpcHModGhpcy5lbGVtZW50KVswXS5lbmFibGUoKVxuICAgIGVsc2VcbiAgICAgIGF0b20udG9vbHRpcHMuZmluZFRvb2x0aXBzKHRoaXMuZWxlbWVudClbMF0uZGlzYWJsZSgpXG4gIH1cblxuICB0b0NsaXBib2FyZCh0b1NldCkge1xuICAgIGlmICh0b1NldCkge1xuICAgICAgdGhpcy5lbGVtZW50Lm9uY29udGV4dG1lbnUgPSAoKSA9PiB7XG4gICAgICAgIGF0b20uY2xpcGJvYXJkLndyaXRlKHRoaXMuZ2V0RGF0ZSh0aGlzLmxvY2FsZSwgdGhpcy50b29sdGlwRGF0ZUZvcm1hdCkpXG4gICAgICAgIGF0b20ubm90aWZpY2F0aW9ucy5hZGRTdWNjZXNzKCdDdXJyZW50IHRpbWUgY29waWVkIHRvIGNsaXBib2FyZC4nLCB7XG4gICAgICAgICAgZGlzbWlzc2FibGU6IHRydWUsXG4gICAgICAgICAgaWNvbjogJ2Nsb2NrJ1xuICAgICAgICB9KVxuICAgICAgfVxuICAgIH0gZWxzZSB7XG4gICAgICB0aGlzLmVsZW1lbnQub25jb250ZXh0bWVudSA9IG51bGxcbiAgICB9XG4gIH1cblxuICBzZXRVVENDbGFzcyh0b1NldCkge1xuICAgIGlmICh0b1NldCkge1xuICAgICAgdGhpcy5lbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2F0b20tY2xvY2stdXRjJylcbiAgICAgIGF0b20udG9vbHRpcHMuZmluZFRvb2x0aXBzKHRoaXMuZWxlbWVudClbMF0uZ2V0VG9vbHRpcEVsZW1lbnQoKS5jbGFzc0xpc3QuYWRkKCdhdG9tLWNsb2NrLXV0YycpXG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMuZWxlbWVudC5jbGFzc0xpc3QucmVtb3ZlKCdhdG9tLWNsb2NrLXV0YycpXG4gICAgICBhdG9tLnRvb2x0aXBzLmZpbmRUb29sdGlwcyh0aGlzLmVsZW1lbnQpWzBdLmdldFRvb2x0aXBFbGVtZW50KCkuY2xhc3NMaXN0LnJlbW92ZSgnYXRvbS1jbG9jay11dGMnKVxuICAgIH1cbiAgfVxuXG5cbiAgdG9nZ2xlKCkge1xuICAgIHZhciBzdHlsZSA9IHRoaXMuZWxlbWVudC5zdHlsZS5kaXNwbGF5XG4gICAgdGhpcy5lbGVtZW50LnN0eWxlLmRpc3BsYXkgPSBzdHlsZSA9PT0gJ25vbmUnID8gJycgOiAnbm9uZSdcbiAgfVxuXG4gIGRlc3Ryb3koKSB7XG4gICAgdGhpcy5jbGVhclRpY2tlcigpXG4gICAgdGhpcy5zdWJzY3JpcHRpb25zLmRpc3Bvc2UoKVxuICAgIHRoaXMudG9vbHRpcC5kaXNwb3NlKClcbiAgICB0aGlzLmVsZW1lbnQucmVtb3ZlKClcbiAgfVxufVxuIl19