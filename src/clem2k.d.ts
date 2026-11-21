import type * as React from 'react';
type Node = React.ReactNode;
export type IconName = 'terminal'|'code'|'file'|'folder'|'search'|'home'|'settings'|'user'|'bot'|'server'|'network'|'chip'|'lock'|'power'|'download'|'play'|'branch'|'trash'|'check'|'close'|'info'|'warning'|'error'|'rain'|'tie';
export type Tone = 'ok'|'warn'|'info'|'err';
export interface IconProps { name: IconName; /** snapped to 12, 24, 36, 48 */ size?: number; label?: string; color?: string; className?: string }
export interface GlassProps extends React.HTMLAttributes<HTMLElement> { as?: string; shape?: 'xl'|'lg'|'pill' }
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { variant?: 'primary'|'secondary'|'ghost'|'danger'|'glass'; size?: 'sm'|'lg'; icon?: IconName }
export interface IconButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { icon: IconName; label: string; variant?: 'ghost'|'secondary'|'primary'|'glass'; size?: 'sm' }
export type Option = string | { value: string; label: Node };
export interface SegmentedControlProps { options: Option[]; value?: string; defaultValue?: string; onChange?(v: string): void; label?: string }
export interface SwitchProps { label?: Node; checked?: boolean; defaultChecked?: boolean; onChange?(v: boolean): void; disabled?: boolean }
export interface FieldProps { label?: Node; help?: Node; error?: string }
export interface TextFieldProps extends FieldProps, React.InputHTMLAttributes<HTMLInputElement> { prompt?: boolean }
export interface TextAreaProps extends FieldProps, React.TextareaHTMLAttributes<HTMLTextAreaElement> {}
export interface SelectProps extends FieldProps, React.SelectHTMLAttributes<HTMLSelectElement> { options: Option[] }
export interface CheckboxProps extends React.InputHTMLAttributes<HTMLInputElement> { label?: Node }
export interface RadioGroupProps { label?: Node; options: Option[]; value?: string; defaultValue?: string; onChange?(v: string): void }
export interface SliderProps { label?: Node; min?: number; max?: number; step?: number; value?: number; defaultValue?: number; onChange?(v: number): void; format?(v: number): Node }
export interface SearchFieldProps extends React.InputHTMLAttributes<HTMLInputElement> { onGlass?: boolean; label?: string }
export interface NavBarProps { brand?: Node; logo?: string; homeHref?: string; links?: { label: Node; href: string; current?: boolean }[]; actions?: Node }
export interface TabsProps { tabs: { id: string; label: Node; content?: Node }[]; value?: string; defaultValue?: string; onChange?(id: string): void }
export interface BreadcrumbsProps { items: { label: Node; href?: string }[] }
export interface PaginationProps { pages: number; page?: number; defaultPage?: number; onChange?(p: number): void }
export interface FooterProps { brand?: Node; tagline?: Node; legal?: Node; columns?: { title: string; links: { label: string; href?: string }[] }[] }
export interface WindowProps { title: string; sidebar?: Node; toolbar?: Node; statusbar?: Node; titlebarStart?: Node; titlebarEnd?: Node; children?: Node; style?: React.CSSProperties; onMinimize?(): void; onMaximize?(): void; onClose?(): void }
export interface ToolbarProps { label?: string; children?: Node }
export interface SidebarItem { label: string; icon?: IconName; href?: string; current?: boolean; count?: number; onClick?(): void }
export interface SidebarProps { sections: { title?: string; items: SidebarItem[] }[]; floating?: boolean }
export interface StatusBarProps { left?: Node[]; right?: Node[]; online?: boolean }
export interface DockProps { label?: string; items: ({ label: string; icon: IconName; current?: boolean; onClick?(): void } | '-')[] }
export interface CommandItem { label: string; icon?: IconName; hint?: string }
export interface CommandPaletteProps { items: CommandItem[]; onSelect?(item: CommandItem): void; placeholder?: string; autoFocus?: boolean }
export interface MenuProps { items: ({ label: string; icon?: IconName; shortcut?: string; danger?: boolean; onClick?(): void } | '-')[] }
export interface CardProps { title?: Node; meta?: Node; children?: Node; actions?: Node; href?: string }
export interface BadgeProps { tone?: 'neutral'|Tone|'bot'; solid?: boolean; icon?: IconName; children?: Node }
export interface AvatarProps { src?: string; name?: string; size?: number; online?: boolean; bot?: boolean }
export interface KbdProps { children?: Node }
export interface TableColumn<R = any> { key: string; label: Node; numeric?: boolean; render?(row: R): Node }
export interface TableProps<R = any> { columns: TableColumn<R>[]; rows: R[]; selected?: string|number; caption?: Node }
export interface CodeBlockProps { code: string; title?: string; lang?: string; lineNumbers?: boolean; copy?: boolean }
export interface TerminalProps { lines: (string | { prompt?: string; tone?: Tone|'mut'; text: Node })[]; prompt?: string; cursor?: boolean }
export interface HeroProps { title: Node; eyebrow?: Node; text?: Node; actions?: Node; aside?: Node }
export interface EmptyStateProps { title: Node; text?: Node; icon?: IconName; action?: Node }
export interface AlertProps { tone?: Tone; title?: Node; children?: Node }
export interface ToastProps { tone?: Tone; children?: Node; action?: Node; onClose?(): void }
export interface ProgressProps { value?: number; label?: string }
export interface SpinnerProps { label?: Node }
export interface SkeletonProps { width?: number|string; height?: number|string; circle?: boolean }
export interface TooltipProps { content: Node; children: Node; open?: boolean }
export interface DialogProps { open: boolean; title?: string; children?: Node; actions?: Node; onClose?(): void; inline?: boolean }
type C<P> = (props: P) => React.ReactElement | null;
declare global { interface Window { clem2k: {
  Icon: C<IconProps> & { names: IconName[] }; Glass: C<GlassProps>; Button: C<ButtonProps>; IconButton: C<IconButtonProps>;
  SegmentedControl: C<SegmentedControlProps>; Switch: C<SwitchProps>; TextField: C<TextFieldProps>; TextArea: C<TextAreaProps>;
  Select: C<SelectProps>; Checkbox: C<CheckboxProps>; RadioGroup: C<RadioGroupProps>; Slider: C<SliderProps>; SearchField: C<SearchFieldProps>;
  NavBar: C<NavBarProps>; Tabs: C<TabsProps>; Breadcrumbs: C<BreadcrumbsProps>; Pagination: C<PaginationProps>; Footer: C<FooterProps>;
  Window: C<WindowProps>; Toolbar: C<ToolbarProps> & { Separator: C<{}> }; Sidebar: C<SidebarProps>; StatusBar: C<StatusBarProps>;
  Dock: C<DockProps>; CommandPalette: C<CommandPaletteProps>; Menu: C<MenuProps>; Card: C<CardProps>; Badge: C<BadgeProps>;
  Avatar: C<AvatarProps>; Kbd: C<KbdProps>; Table: C<TableProps>; CodeBlock: C<CodeBlockProps>; Terminal: C<TerminalProps>;
  Hero: C<HeroProps>; EmptyState: C<EmptyStateProps>; Alert: C<AlertProps>; Toast: C<ToastProps>; Progress: C<ProgressProps>;
  Spinner: C<SpinnerProps>; Skeleton: C<SkeletonProps>; Tooltip: C<TooltipProps>; Dialog: C<DialogProps>;
} } }
